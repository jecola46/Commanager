import tkinter as tk
import math
from .deck_lister import DeckLister

class MainAppUI(tk.Tk):
    def __init__(self, deck_collection):
        super().__init__()
        self.title("MTG Deck Manager")

        self.deck_collection = deck_collection

        self.create_widgets()

    def create_widgets(self):
        deck_list_label = tk.Label(self, text="Your decks", font=("Helvetica", 24))
        deck_list_label.grid(row=0, column=1, pady=10, sticky='ew')

        self.create_filter_ui()

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        deck_list = self.deck_collection.get_deck_summaries()
        self.deck_lister = DeckLister(self, deck_list, self.deck_collection)
        self.deck_lister.grid(row=1, column=1, sticky='nsew')

        # Add a scrollbar
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.deck_lister.yview)
        scrollbar.grid(row=1, column=2, sticky='ns')
        self.deck_lister.configure(yscrollcommand=scrollbar.set)

    def create_filter_ui(self):
        pass