import tkinter as tk
from deck_io import save_decks_to_file
from deck_analysis_utils import DISPLAY_TO_INTERNAL_COLOR
from deck_io.deck_io import load_custom_filters, save_new_filter
from ui_elements.custom_sort_window import CustomSortWindow

class FilterAndSortPanel(tk.Frame):
    def __init__(self, root, deck_collection):
        super().__init__(root)
        self.root = root
        self.deck_collection = deck_collection
        self.creating_sort = False
        self.sort_vars = {}
        self.individual_card_sort_functions = {}
        self.create_filter_ui()
        self.create_sort_ui()
        self.create_save_and_stats_ui()

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
        sort_label = tk.Label(self, text="Sort by Property", font=("Helvetica", 12, "bold"))
        sort_label.pack(side=tk.TOP)

        card_filters = load_custom_filters(self.deck_collection.get_user())
        for filter in card_filters:
            filter_name = filter['name']
            filter_var = tk.BooleanVar()
            checkbutton = tk.Checkbutton(self, text=filter_name, variable=filter_var, command=self.filter_and_sort_decks)
            checkbutton.pack(anchor='w')
            self.sort_vars[filter_name] = filter_var
            self.individual_card_sort_functions[filter_name] = filter['function']

        self.add_sort_button = tk.Button(self, text='+ Custom', height=2, width=10, command=self.add_custom_sort, bg='blue')
        self.add_sort_button.pack(anchor='w')

    def add_custom_sort(self):
        pass
    
    def sort_by_custom_card_filter(self, filtered_decks, filter):
        sorted_decks = []
        for deck in filtered_decks:
            public_id = deck.get('publicId', '')
            count = self.deck_collection.count_cards_with_property(public_id, filter)
            sorted_decks.append((deck, count))

        sorted_decks.sort(key=lambda x: x[1], reverse=True)
        return sorted_decks

    def filter_and_sort_decks(self):
        filtered_decks = self.get_filtered_decks()
        if self.is_sorting_enabled():
            custom_sort_name = self.get_first_checked_sort()
            sorted_decks = self.sort_by_custom_card_filter(filtered_decks, self.individual_card_sort_functions[custom_sort_name])
            self.root.update_deck_lister_with_count(sorted_decks)
        else:
            self.root.update_deck_lister(filtered_decks)

    def get_first_checked_sort(self):
        for sort_var_name in self.sort_vars.keys():
            if self.sort_vars[sort_var_name].get():
                return sort_var_name
        return None

    def is_sorting_enabled(self):
        return self.get_first_checked_sort() is not None

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

    def create_save_and_stats_ui(self):
        self.swap_user_button = tk.Button(self, text='Swap User Data', height=2, width=10, command=self.save_and_swap_collection, bg='red')
        self.swap_user_button.pack(side=tk.BOTTOM)

    def save_and_swap_collection(self):
        save_decks_to_file(self.deck_collection.get_deck_summaries(), self.deck_collection.get_deck_details())
        self.root.return_to_deck_loader()

    def add_custom_sort(self):
        rule_var = tk.StringVar()
        custom_sort_window = CustomSortWindow(self, rule_var)
        self.wait_window(custom_sort_window)
        print(f"Created rule: {rule_var.get()}")
        filter_var = tk.BooleanVar()
        checkbutton = tk.Checkbutton(self, text=rule_var.get(), variable=filter_var, command=self.filter_and_sort_decks)
        checkbutton.pack(anchor='w')
        self.sort_vars[rule_var.get()] = filter_var
        new_filter = save_new_filter(self.deck_collection.get_user(), rule_var.get(), rule_var.get())
        self.individual_card_sort_functions[rule_var.get()] = new_filter['function']