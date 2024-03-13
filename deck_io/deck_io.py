import json
import requests
import time
import requests
import os
import re
from PIL import Image, ImageTk
from io import BytesIO

def grab_decks_from_moxfield(username):
    """
    Fetches deck summaries and details from Moxfield API for a given username.

    Args:
    - username (str): The Moxfield username.

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
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            decks_json = response.json()

            deck_summaries = decks_json['data']
            deck_details = {}
            for deck in deck_summaries:
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
            print(f"Failed to fetch decks. Status Code: {response}")
            print(f"Failed to fetch decks. Status Code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

def load_decks_from_file(summary_filename='deck_summaries.json', details_filename='deck_details.json'):
    """
    Loads deck summaries and details from specified JSON files.

    Args:
    - summary_filename (str): The filename for deck summaries JSON file (default is 'deck_summaries.json').
    - details_filename (str): The filename for deck details JSON file (default is 'deck_details.json').

    Returns:
    - Tuple: A tuple containing deck summaries and details.
      - deck_summaries (list): List of deck summaries loaded from the file.
      - deck_details (dict): Dictionary containing deck details loaded from the file.

    If a file is not found, an empty list or dictionary is returned accordingly.
    """
    deck_summaries = []
    deck_details = {}
    try:
        with open(summary_filename, 'r') as file:
            deck_summaries = json.load(file)
        deck_summaries = deck_summaries
    except FileNotFoundError:
        print(f"File '{summary_filename}' not found.")
        return []

    try:
        with open(details_filename, 'r') as file:
            deck_details = json.load(file)
        deck_details = deck_details
    except FileNotFoundError:
        print(f"File '{details_filename}' not found.")
        return []
    return deck_summaries, deck_details

def save_decks_to_file(deck_summaries, deck_details, summary_filename='deck_summaries.json', details_filename='deck_details.json'):
        with open(summary_filename, 'w') as file:
            json.dump(deck_summaries, file)

        with open(details_filename, 'w') as file:
            json.dump(deck_details, file)

def fetch_card_image_from_scryfall(card_name):
    # Create a directory for caching if it doesn't exist
    cache_folder = "image_cache"
    if not os.path.exists(cache_folder):
        os.makedirs(cache_folder)

    # Check if the image is already cached
    cache_file_path = os.path.join(cache_folder, sanitize_filename(f"{card_name}.jpg"))
    if os.path.exists(cache_file_path):
        image = Image.open(cache_file_path)
        photo_image = ImageTk.PhotoImage(image)
        return photo_image

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

            image, image_data = get_image_from_url(card_image_url)
            with open(cache_file_path, 'wb') as f:
                    f.write(image_data)
            return image

        else:
            print(f"Failed to get card art. Status Code: {response}")
            print(f"Failed to get card art. Status Code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

def sanitize_filename(filename):
    # Remove invalid characters from the filename
    sanitized_filename = re.sub(r'[\\/:"?*<>|]', '_', filename)
    return sanitized_filename

def get_image_from_url(url):
        print(url)
        try:
            response = requests.get(url)
            image_data = response.content
            image = Image.open(BytesIO(image_data))
            image = ImageTk.PhotoImage(image)
            return image, image_data
        except Exception as e:
            print("Error loading image:", e)
            return None