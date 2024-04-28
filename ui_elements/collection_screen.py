import tkinter as tk
import math
from .deck_lister import DeckLister
from deck_analysis_utils import DISPLAY_TO_INTERNAL_COLOR
from deck_io import save_decks_to_file

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

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        deck_list = self.deck_collection.get_deck_summaries()
        self.deck_lister = DeckLister(self, deck_list, self.deck_collection)
        self.displayed_decks = deck_list
        self.deck_lister.grid(row=1, column=1, sticky='nsew')

        # Add a scrollbar
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.deck_lister.yview)
        self.scrollbar.grid(row=1, column=2, sticky='ns')
        self.deck_lister.configure(yscrollcommand=self.scrollbar.set)

    def create_filter_and_sort_ui(self):
        filter_and_sort_frame = tk.Frame(self)
        filter_and_sort_frame.grid(row=1, column=0, padx=10, pady=10, sticky='n')
        self.create_filter_ui(filter_and_sort_frame)
        self.create_sort_ui(filter_and_sort_frame)
        self.create_save_and_stats_ui(filter_and_sort_frame)

    def create_filter_ui(self, root):
        # Define a dictionary to store the filter variables
        self.filter_vars = {
            "White": tk.BooleanVar(),
            "Blue": tk.BooleanVar(),
            "Black": tk.BooleanVar(),
            "Green": tk.BooleanVar(),
            "Red": tk.BooleanVar()
        }

        filter_label = tk.Label(root, text="Filter by Color", font=("Helvetica", 12, "bold"))
        filter_label.pack(side=tk.TOP)

        for color in self.filter_vars:
            checkbutton = tk.Checkbutton(root, text=color, variable=self.filter_vars[color], command=self.filter_and_sort_decks)
            checkbutton.pack(anchor='w')

    def create_sort_ui(self, root):
        sort_label = tk.Label(root, text="Sort by Property", font=("Helvetica", 12, "bold"))
        sort_label.pack(side=tk.TOP)

        self.outlaw_count_sort = tk.BooleanVar()
        checkbutton = tk.Checkbutton(root, text='Sort by Outlaws', variable=self.outlaw_count_sort, command=self.filter_and_sort_decks)
        checkbutton.pack(anchor='w')

    def filter_and_sort_decks(self):
        filtered_decks = self.get_filtered_decks()
        if self.is_sorting_enabled():
            sorted_decks = self.sort_by_outlaws()
            self.update_deck_lister_with_count(sorted_decks)
        else:
            self.update_deck_lister(self.get_filtered_decks())

    def sort_by_outlaws(self):
        def is_outlaw(card_item):
            if 'card' in card_item and 'type_line' in card_item['card']:
                type_line = card_item['card']['type_line']
                return "Assassin" in type_line or "Mercenary" in type_line or "Pirate" in type_line or "Rogue" in type_line or "Warlock" in type_line
            return False

        if self.outlaw_count_sort.get():
            filtered_decks = self.get_filtered_decks()
            sorted_decks = []
            for deck in filtered_decks:
                public_id = deck.get('publicId', '')
                count = self.deck_collection.count_cards_with_property(public_id, is_outlaw)
                sorted_decks.append((deck, count))

            sorted_decks.sort(key=lambda x: x[1], reverse=True)
            return sorted_decks

    def is_sorting_enabled(self):
        return self.outlaw_count_sort is not None and self.outlaw_count_sort.get()

    def get_filtered_decks(self):
        deck_list = self.deck_collection.get_deck_summaries()
        deck_colors_map = self.deck_collection.get_deck_colors_map()

        # Filter decks based on selected colors
        filtered_decks = []
        for deck in deck_list:
            colors_set = set(deck_colors_map.get(deck.get('publicId', '')))
            selected_colors = {DISPLAY_TO_INTERNAL_COLOR[color] for color, var in self.filter_vars.items() if var.get()}
            if selected_colors.issubset(colors_set):
                filtered_decks.append(deck)

        return filtered_decks

    def update_deck_lister(self, new_decks):
        self.deck_lister.destroy()
        self.deck_lister = DeckLister(self, new_decks, self.deck_collection)
        self.displayed_decks = new_decks
        self.deck_lister.grid(row=1, column=1, sticky='nsew')

        self.deck_lister.configure(yscrollcommand=self.scrollbar.set)
        # Need these for some reason to get the scrollbar working correctly
        self.update_idletasks()
        self.deck_lister.update_things()

    def update_deck_lister_with_count(self, new_decks_and_count):
        self.deck_lister.destroy()
        self.deck_lister = DeckLister(self, new_decks_and_count, self.deck_collection)
        new_decks, count = zip(*new_decks_and_count)
        self.displayed_decks = new_decks
        self.deck_lister.grid(row=1, column=1, sticky='nsew')

        self.deck_lister.configure(yscrollcommand=self.scrollbar.set)
        # Need these for some reason to get the scrollbar working correctly
        self.update_idletasks()
        self.deck_lister.update_things()

    def show_deck_details(self, deck):
        self.root.show_deck_details_screen(deck, self.displayed_decks)

    def create_save_and_stats_ui(self, root): 
        self.swap_user_button = tk.Button(root, text='Swap User Data', height=2, width=10, command=self.save_and_swap_collection, bg='red')
        self.swap_user_button.pack(side=tk.BOTTOM)

    def save_and_swap_collection(self):
        save_decks_to_file(self.deck_collection.get_deck_summaries(), self.deck_collection.get_deck_details())
        self.root.return_to_deck_loader()