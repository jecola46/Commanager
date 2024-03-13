import tkinter as tk
from deck_io import fetch_card_image_from_scryfall

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
        self.back_button = tk.Button(self, text="Back", command=self.back_pressed)
        self.back_button.pack(side=tk.TOP, pady=10)

        # Create and place widgets to display deck details
        self.deck_name_label = tk.Label(self, text=deck['name'], font=('Helvetica', 18, 'bold'))
        self.deck_name_label.pack(pady=(10, 5))

        # Wrap text in description label
        self.deck_description_label = tk.Label(self, text=deck_collection.get_deck_description(deck['publicId']),
                                                wraplength=500, justify='left')
        self.deck_description_label.pack(padx=10, pady=5)

        commander_card_name = self.deck_collection.get_deck_commander_name(deck['publicId'])

        image = fetch_card_image_from_scryfall(commander_card_name)
        if image:
            self.commander_image_label = tk.Label(self, image=image)
            self.commander_image_label.image = image  # Keep a reference to prevent garbage collection
            self.commander_image_label.pack(pady=10)
            print("packed")

    def back_pressed(self):
        self.back_button.destroy()
        self.deck_name_label.destroy()
        self.deck_description_label.destroy()
        self.commander_image_label.destroy()
        self.back_callback()