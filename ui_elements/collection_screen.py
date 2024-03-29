import tkinter as tk
import math
from .deck_lister import DeckLister
from deck_analysis_utils import DISPLAY_TO_INTERNAL_COLOR

class CollectionScreen(tk.Frame):
    def __init__(self, root, deck_collection):
        super().__init__(root)
        self.root = root

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
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.deck_lister.yview)
        self.scrollbar.grid(row=1, column=2, sticky='ns')
        self.deck_lister.configure(yscrollcommand=self.scrollbar.set)

    def create_filter_ui(self):
        # Define a dictionary to store the filter variables
        self.filter_vars = {
            "White": tk.BooleanVar(),
            "Blue": tk.BooleanVar(),
            "Black": tk.BooleanVar(),
            "Green": tk.BooleanVar(),
            "Red": tk.BooleanVar()
        }

        # Create filter labels and checkbuttons for each color
        filter_frame = tk.Frame(self)
        filter_frame.grid(row=1, column=0, padx=10, pady=10, sticky='n')

        filter_label = tk.Label(filter_frame, text="Filter by Color", font=("Helvetica", 12, "bold"))
        filter_label.pack(side=tk.TOP)

        for color in self.filter_vars:
            checkbutton = tk.Checkbutton(filter_frame, text=color, variable=self.filter_vars[color], command=self.apply_filters)
            checkbutton.pack(anchor='w')

    def apply_filters(self):
        deck_list = self.deck_collection.get_deck_summaries()
        deck_colors_map = self.deck_collection.get_deck_colors_map()

        # Filter decks based on selected colors
        filtered_decks = []
        for deck in deck_list:
            colors_set = set(deck_colors_map.get(deck.get('publicId', '')))
            selected_colors = {DISPLAY_TO_INTERNAL_COLOR[color] for color, var in self.filter_vars.items() if var.get()}
            if selected_colors.issubset(colors_set):
                filtered_decks.append(deck)

        self.update_deck_lister(filtered_decks)

    def update_deck_lister(self, new_decks):
        self.deck_lister.destroy()
        self.deck_lister = DeckLister(self, new_decks, self.deck_collection)
        self.deck_lister.grid(row=1, column=1, sticky='nsew')

        self.deck_lister.configure(yscrollcommand=self.scrollbar.set)
        # Need these for some reason to get the scrollbar working correctly
        self.update_idletasks()
        self.deck_lister.update_things()