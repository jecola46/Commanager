import tkinter as tk

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