import tkinter as tk
from deck_io import save_decks_to_file
from deck_analysis_utils import DISPLAY_TO_INTERNAL_COLOR
from ui_elements.sort_panel import SortPanel

class FilterAndSortPanel(tk.Frame):
    def __init__(self, root, deck_collection):
        super().__init__(root)
        self.root = root
        self.deck_collection = deck_collection
        self.creating_sort = False
        self.create_filter_ui()
        self.create_sort_ui()

    def create_filter_ui(self):
        # Define a dictionary to store the filter variables
        self.filter_vars = {
            "White": tk.BooleanVar(),
            "Blue": tk.BooleanVar(),
            "Black": tk.BooleanVar(),
            "Green": tk.BooleanVar(),
            "Red": tk.BooleanVar()
        }

        filter_label = tk.Label(self, text="Filter by Color", font=("Helvetica", 12, "bold"))
        filter_label.pack(side=tk.TOP)

        for color in self.filter_vars:
            checkbutton = tk.Checkbutton(self, text=color, variable=self.filter_vars[color], command=self.filter_and_sort_decks)
            checkbutton.pack(anchor='w')

    def create_sort_ui(self):
        self.sort_panel = SortPanel(self, self.deck_collection, self.filter_and_sort_decks)
        self.sort_panel.pack(side=tk.TOP, fill=tk.X)

    def filter_and_sort_decks(self):
        filtered_decks = self.get_filtered_decks()
        sorted_decks = self.sort_panel.sort_decks(filtered_decks)
        self.root.update_deck_lister(sorted_decks)

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
