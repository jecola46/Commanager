import tkinter as tk
import math
from .deck_lister import DeckLister
from .filter_and_sort_panel import FilterAndSortPanel
from .save_and_stats_panel import SaveAndStatsPanel

class CollectionScreen(tk.Frame):
    def __init__(self, root, deck_collection):
        super().__init__(root)
        self.root = root

        self.deck_collection = deck_collection

        self.create_widgets()

    def create_widgets(self):
        deck_list_label = tk.Label(self, text="Your decks", font=("Helvetica", 24))
        deck_list_label.grid(row=0, column=1, pady=10, sticky='ew')

        self.create_filter_and_sort_ui()
        self.create_save_and_stats_ui()

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        deck_list = self.deck_collection.get_deck_summaries()
        self.deck_lister = DeckLister(self, deck_list, self.deck_collection)
        self.displayed_decks = deck_list
        self.deck_lister.grid(row=1, column=1, sticky='nsew', rowspan=2)

        # Add a scrollbar
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.deck_lister.yview)
        self.scrollbar.grid(row=1, column=2, sticky='ns', rowspan=2)
        self.deck_lister.configure(yscrollcommand=self.scrollbar.set)

    def create_filter_and_sort_ui(self):
        filter_and_sort_frame = FilterAndSortPanel(self, self.deck_collection)
        filter_and_sort_frame.grid(row=1, column=0, padx=10, pady=10, sticky='ns')

    def update_deck_lister(self, new_decks):
        self.deck_lister.destroy()
        self.deck_lister = DeckLister(self, new_decks, self.deck_collection)
        self.displayed_decks = new_decks
        self.deck_lister.grid(row=1, column=1, sticky='nsew', rowspan=2)

        self.deck_lister.configure(yscrollcommand=self.scrollbar.set)
        # Need these for some reason to get the scrollbar working correctly
        self.update_idletasks()
        self.deck_lister.update_things()

    def update_deck_lister_with_count(self, new_decks_and_count):
        self.deck_lister.destroy()
        self.deck_lister = DeckLister(self, new_decks_and_count, self.deck_collection)
        new_decks, count = zip(*new_decks_and_count)
        self.displayed_decks = new_decks
        self.deck_lister.grid(row=1, column=1, sticky='nsew', rowspan=2)

        self.deck_lister.configure(yscrollcommand=self.scrollbar.set)
        # Need these for some reason to get the scrollbar working correctly
        self.update_idletasks()
        self.deck_lister.update_things()

    def create_save_and_stats_ui(self):
        save_and_stats_frame = SaveAndStatsPanel(self, self.deck_collection)
        save_and_stats_frame.grid(row=2, column=0, padx=10, pady=10, sticky='s')

    def show_deck_details(self, deck):
        self.root.show_deck_details_screen(deck, self.displayed_decks)

    def return_to_deck_loader(self):
        self.root.return_to_deck_loader()

    def show_collection_analysis_screen(self):
        # Implement the logic to show the deck analysis screen
        pass