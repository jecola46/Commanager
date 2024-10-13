import json
import requests
import time
import requests
import os
import re
from PIL import Image, ImageTk
from io import BytesIO
from threading import Thread
from pathlib import Path
from grammar import create_filter_from_string

USER_DATA_ROOT = Path('user_data')
MOST_RECENT_USER_FILE = USER_DATA_ROOT / 'most_recent_user.txt'

def user_data_folder(username):
    return USER_DATA_ROOT / username

def deck_summary_file_path(username):
    return USER_DATA_ROOT / username / 'deck_summaries.json'

def deck_details_file_path(username):
    return USER_DATA_ROOT / username / 'deck_details.json'

def custom_filters_file_path(username):
    return USER_DATA_ROOT / username / 'custom_filters.json'
        
def grab_decks_from_moxfield(username, update_loading_callback):
    """
    Fetches deck summaries and details from Moxfield API for a given username.

    Args:
    - username (str): The Moxfield username.
    - update_loading_callback (function(str label, num percent_increase)): A callback to update loading bar.
    Takes a label for the ongoing work and a percentage to increase loading bar.

    Returns:
    - Tuple: A tuple containing deck summaries and details.
      - deck_summaries (list): List of deck summaries (basic information).
      - deck_details (dict): Dictionary containing detailed information for each deck, keyed by deck ID.
    """
    api_url = f"https://api.moxfield.com/v2/users/{username}/decks?pageNumber=1&pageSize=99999"

    # Define headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        update_loading_callback('Retreiving list of decks', 0)
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            decks_json = response.json()
            
            def is_legal_commander_deck(deck_summary):
                return deck_summary['format'] == 'commander' and deck_summary['isLegal']

            def is_illegal_commander_deck(deck_summary):
                return deck_summary['format'] == 'commander' and not deck_summary['isLegal']

            deck_summaries = list(filter(is_legal_commander_deck, decks_json['data']))
            illegal_deck_summaries = list(filter(is_illegal_commander_deck, decks_json['data']))
            print(f'Illegal commander decks are {list(map(lambda summary: summary["name"], illegal_deck_summaries))}')
            deck_details = {}
            deck_num = 0
            for deck in deck_summaries:
                deck_num += 1
                update_loading_callback(f'({deck_num} / {len(deck_summaries)}) Retreiving deck: {deck["name"]} ', 100 / len(deck_summaries))
                time.sleep(1)
                deck_id = deck['publicId']
                api_url = f"https://api.moxfield.com/v2/decks/all/{deck_id}"
                response = requests.get(api_url, headers=headers)
                if response.status_code == 200:
                    deck_json = response.json()
                    deck_details[deck_id] = deck_json
                else:
                    print(f"Failed to fetch deck: {deck.name}. Status Code: {response}")
                    print(f"Failed to fetch deck: {deck.name}. Status Code: {response.status_code}")

            return deck_summaries, deck_details

        else:
            print(f"Failed to get user decks. Response: {response} Status Code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

def load_decks_from_file(username):
    """
    Loads deck summaries and details for a specific user.

    Args:
    - username (str): The folder in which the deck_summaries.json and deck_details.json file are to be retrieved from.

    Returns:
    - Tuple: A tuple containing deck summaries and details.
      - deck_summaries (list): List of deck summaries loaded from the file.
      - deck_details (dict): Dictionary containing deck details loaded from the file.

    If data is not found, an empty list or dictionary is returned accordingly.
    """
    if not user_data_folder(username).is_dir():
        print(f"No data for user '{username}'.")
        return []
    
    deck_summaries = []
    deck_details = {}
    try:
        # see existing folders and pick one, or save most recent
        # can username ever be undefined?
        raw_deck_summary = deck_summary_file_path(username).read_text()
        deck_summaries = json.loads(raw_deck_summary)
    except FileNotFoundError:
        # Needs to be tested with pathlib -- COMM-23
        print(f"File '{deck_summary_file_path(username)}' not found.")
        return []

    try:
        raw_deck_details = deck_details_file_path(username).read_text()
        deck_details = json.loads(raw_deck_details)
    except FileNotFoundError:
        # Needs to be tested with pathlib -- COMM-23
        print(f"File '{deck_details_file_path(username)}' not found.")
        return []
    return deck_summaries, deck_details

def save_decks_to_file(deck_summaries, deck_details):
    """
    Saves deck summaries and deck details to users folder.

    Args:
    - deck_summaries (list): List of deck summaries for user.
    - deck_details (dict): Dictionary containing deck details for user.
    """
    username = deck_summaries[0]['createdByUser']['userName']
    
    if not user_data_folder(username).is_dir():
        user_data_folder(username).mkdir()
        
    deck_summary_file_path(username).write_text(json.dumps(deck_summaries))   
    deck_details_file_path(username).write_text(json.dumps(deck_details))

def fetch_card_image_from_scryfall(card_name, resize):
    """
    Fetches the given card image from scryfall, with optional resize.

    Args:
    - card_name (str): Card name to fetch.
    - resize (tuple(width, height)): A tuple containing the desired (width, height) to which the image will be resized.

    Returns:
    - Tuple: a Tuple containing the desired image and whether or not that image came from the cache.
        - image (ImageTK.PhotoImage): The desired image.
        - from_cache (bool): Whether or not the image came from the cache.
    """
    # Create a directory for caching if it doesn't exist
    cache_folder = Path("image_cache")
    if not os.path.exists(cache_folder):
        os.makedirs(cache_folder)

    # Check if the image is already cached
    cache_file_path = cache_folder / sanitize_filename(f'{card_name}.jpg')

    if os.path.exists(cache_file_path):
        image = Image.open(cache_file_path)
        image = image.resize(resize)
        photo_image = ImageTk.PhotoImage(image)
        return photo_image, True

    api_url = f'https://api.scryfall.com/cards/named?exact={card_name}'
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            card_json = response.json()
            card_image_url = ''
            if 'image_uris' in card_json:
                card_image_url =  card_json['image_uris']['normal']
            else:
                card_image_url = card_json['card_faces'][0]['image_uris']['normal']

            image, image_data = get_image_from_url(card_image_url, resize)

            cache_file_path.write_bytes(image_data)
            return image, False

        else:
            print(f"Failed to get card art. Response: {response} Status Code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

def grab_card_image_async(image_labels):
    art_grab_thread = GetCardImageForLabels(image_labels)
    art_grab_thread.start()

class GetCardImageForLabels(Thread):
    def __init__(self, image_labels):
        super().__init__()
        self.image_labels = image_labels

    def run(self):
        # Assume the first image label is the main one to display and should be larger
        for i, image_label in enumerate(self.image_labels):
            if i == 0:
                image, from_cache = fetch_card_image_from_scryfall(image_label.card_name, (630, 880))
            else:
                image, from_cache = fetch_card_image_from_scryfall(image_label.card_name, (126, 176))
            image_label.config(image=image)
            image_label.image = image
            if not from_cache:
                time.sleep(1)

def fetch_card_art_from_scryfall(card_name, resize = None):
    # Create a directory for caching if it doesn't exist
    cache_folder = Path("image_cache")
    if not os.path.exists(cache_folder):
        os.makedirs(cache_folder)

    # Check if the image is already cached
    cache_file_path = cache_folder / sanitize_filename(f"{card_name}-art.jpg")  # Join file paths, PathLib uses a cute operator
    
    if os.path.exists(cache_file_path):
        image = Image.open(cache_file_path)
        image = image.resize(resize)
        photo_image = ImageTk.PhotoImage(image)
        return photo_image, True

    api_url = f'https://api.scryfall.com/cards/named?exact={card_name}'
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            card_json = response.json()
            card_image_url = ''
            if 'image_uris' in card_json:
                card_image_url =  card_json['image_uris']['art_crop']
            else:
                card_image_url = card_json['card_faces'][0]['image_uris']['art_crop']

            image, image_data = get_image_from_url(card_image_url, resize)
            
            cache_file_path.write_bytes(image_data)
            return image, False

        else:
            print(f"Failed to get card art. Response: {response} Status Code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

def grab_card_art_async(image_labels, resize = None):
    art_grab_thread = GetImageForLabels(image_labels, resize)
    art_grab_thread.start()

class GetImageForLabels(Thread):
    def __init__(self, image_labels, resize = None):
        super().__init__()
        self.image_labels = image_labels
        self.resize = resize

    def run(self):
        for image_label in self.image_labels:
            image, from_cache = fetch_card_art_from_scryfall(image_label.card_art_name, self.resize)
            image_label.config(image=image)
            image_label.image = image
            if not from_cache:
                time.sleep(1)

def sanitize_filename(filename):
    # Remove invalid characters from the filename
    sanitized_filename = re.sub(r'[\\/:"?*<>|]', '_', filename)
    return sanitized_filename

def get_image_from_url(url, resize = None):
        print(url)
        try:
            response = requests.get(url)
            image_data = response.content
            image = Image.open(BytesIO(image_data))
            if resize is not None:
                image = image.resize(resize)
            image = ImageTk.PhotoImage(image)
            return image, image_data
        except Exception as e:
            print("Error loading image:", e)
            return None
        
def load_custom_filters(username):
    filters_file = custom_filters_file_path(username)
    if not filters_file.exists():
        return []
    custom_filters = json.loads(filters_file.read_text())
    for filter in custom_filters:
        filter['function'] = create_filter_from_string(filter['definition'])
    return custom_filters