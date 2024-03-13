import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from deck_io import fetch_card_image_url_from_scryfall

class DeckViewer(tk.Frame):
    def __init__(self, root, deck_collection, deck, back_callback):
        super().__init__(root)
        self.root = root
        self.deck_collection = deck_collection
        self.deck = deck
        self.back_callback = back_callback
        print(deck)

        # Set background color
        self.configure(background='lightgray')

        # Create back button
        self.back_button = tk.Button(self, text="Back", command=self.back_callback)
        self.back_button.pack(side=tk.TOP, pady=10)

        # Create and place widgets to display deck details
        self.deck_name_label = tk.Label(self, text=deck['name'], font=('Helvetica', 18, 'bold'))
        self.deck_name_label.pack(pady=(10, 5))

        # Wrap text in description label
        self.deck_description_label = tk.Label(self, text=deck_collection.get_deck_description(deck['publicId']),
                                                wraplength=500, justify='left')
        self.deck_description_label.pack(padx=10, pady=5)

        commander_card_name = self.deck_collection.get_deck_commander(deck['publicId'])['name']
        commander_image_url = fetch_card_image_url_from_scryfall(commander_card_name)

        image = self.get_image_from_url(commander_image_url)
        if image:
            self.commander_image_label = tk.Label(self, image=image)
            self.commander_image_label.image = image  # Keep a reference to prevent garbage collection
            self.commander_image_label.pack(pady=10)
            print("packed")

    def get_image_from_url(self, url):
        print(url)
        try:
            response = requests.get(url)
            image_data = response.content
            image = Image.open(BytesIO(image_data))
            image = ImageTk.PhotoImage(image)
            return image
        except Exception as e:
            print("Error loading image:", e)
            return None