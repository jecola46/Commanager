import json
import requests
import time

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

def fetch_card_image_url_from_scryfall(card_name):
    api_url = f'https://api.scryfall.com/cards/named?exact={card_name}'
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            card_json = response.json()
            return card_json['image_uris']['normal']

        else:
            print(f"Failed to get card art. Status Code: {response}")
            print(f"Failed to get card art. Status Code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")
