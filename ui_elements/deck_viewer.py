import tkinter as tk

class DeckViewer(tk.Frame):
    def __init__(self, root, deck_collection, deck):
        super().__init__(root)
        self.root = root
        self.deck_collection = deck_collection
        self.deck = deck
        print(deck)

        # Set background color
        self.configure(background='lightgray')

        # Create and place widgets to display deck details
        self.deck_name_label = tk.Label(self, text=deck['name'], font=('Helvetica', 18, 'bold'))
        self.deck_name_label.pack(pady=(10, 5))

        # Wrap text in description label
        self.deck_description_label = tk.Label(self, text=deck_collection.get_deck_description(deck['publicId']),
                                                wraplength=500, justify='left')
        self.deck_description_label.pack(padx=10, pady=5)