import tkinter as tk
from deck_io import save_decks_to_file
from deck_analysis_utils import DISPLAY_TO_INTERNAL_COLOR
from grammar import CustomSortRule

class FilterAndSortPanel(tk.Frame):
    def __init__(self, root, deck_collection):
        super().__init__(root)
        self.root = root
        self.deck_collection = deck_collection
        self.creating_sort = False
        self.create_filter_ui()
        self.create_sort_ui()
        self.create_save_and_stats_ui()
        self.custom_sort = None

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

        self.outlaw_count_sort = tk.BooleanVar()
        checkbutton = tk.Checkbutton(self, text='Sort by Outlaws', variable=self.outlaw_count_sort, command=self.filter_and_sort_decks)
        checkbutton.pack(anchor='w')

        self.add_sort_button = tk.Button(self, text='+ Custom', height=2, width=10, command=self.add_custom_sort, bg='blue')
        self.add_sort_button.pack(anchor='w')

    def add_custom_sort(self):
        if self.creating_sort:
            return
        self.creating_sort = True
        self.add_sort_frame = tk.Frame(self)
        self.add_sort_frame.pack(anchor='w')

        self.customize_sort_frame = tk.Frame(self.add_sort_frame)
        self.customize_sort_frame.grid(row=0, column=0, sticky='nsew')

        self.save_sort_button = tk.Button(self.add_sort_frame, text='Save', height=2, width=10, command=self.save_sort, bg='Green')
        self.save_sort_button.grid(row=1, column=0, sticky='nsew')

        menu_label = tk.Label(self.customize_sort_frame, text="Sort by", font=("Helvetica", 12, "bold"))
        menu_label.grid(row=0, column=0, sticky='nsew')

        self.constructing_sort = CustomSortRule()
        self.custom_sort_next_part(1, self.constructing_sort)

    def custom_sort_next_part(self, row, rule_part):
        if rule_part.is_text_entry():
            self.sort_text_box = tk.Entry(self.customize_sort_frame)
            self.sort_text_box.grid(row=row, column=0, sticky='nsew')
            rule_part.text_box = self.sort_text_box
        else:
            rule_part.clicked = tk.StringVar()

            drop = tk.OptionMenu(self.customize_sort_frame, rule_part.clicked, *rule_part.get_current_option_strings())
            drop.grid(row=row, column=0, sticky='nsew')

            def drop_callback(var, index, mode):
                rule_part.choose_option(rule_part.clicked.get())
                if rule_part.next is not None:
                    self.custom_sort_next_part(row + 1, rule_part.next)

            rule_part.clicked.trace('w', drop_callback)
            rule_part.clicked.set("-")


    def save_sort(self):
        def custom_sort(card_item):
            return self.constructing_sort.should_count_card(card_item)
        self.custom_sort = custom_sort
        self.filter_and_sort_decks()

    def sort_type_selected(self, *args):
        self.sort_type_clicked = tk.StringVar()

    def sort_by_custom(self, filtered_decks):
        sorted_decks = []
        for deck in filtered_decks:
            public_id = deck.get('publicId', '')
            count = self.deck_collection.count_cards_with_property(public_id, self.custom_sort)
            sorted_decks.append((deck, count))

        sorted_decks.sort(key=lambda x: x[1], reverse=True)
        return sorted_decks

    def filter_and_sort_decks(self):
        filtered_decks = self.get_filtered_decks()
        if self.is_sorting_enabled():
            if self.outlaw_count_sort.get():
                sorted_decks = self.sort_by_outlaws()
                self.root.update_deck_lister_with_count(sorted_decks)
            else:
                sorted_decks = self.sort_by_custom(filtered_decks)
                self.root.update_deck_lister_with_count(sorted_decks)
            
        else:
            self.root.update_deck_lister(self.get_filtered_decks())

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
        return self.outlaw_count_sort is not None and self.outlaw_count_sort.get() or self.custom_sort is not None

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
