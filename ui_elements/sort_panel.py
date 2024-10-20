import tkinter as tk
from deck_io.deck_io import load_custom_filters, save_new_filter 
from ui_elements.custom_sort_window import CustomSortWindow
from grammar import validate_filter

class SortPanel(tk.Frame):
    def __init__(self, parent, deck_collection, filter_and_sort_callback):
        super().__init__(parent)
        self.parent = parent
        self.deck_collection = deck_collection
        self.filter_and_sort_callback = filter_and_sort_callback
        self.sort_vars = {}
        self.individual_card_sort_functions = {}
        self.create_ui()

    def create_ui(self):
        sort_label = tk.Label(self, text="Sort by Property", font=("Helvetica", 12, "bold"))
        sort_label.pack(side=tk.TOP)

        card_filters = load_custom_filters(self.deck_collection.get_user())

        self.sort_rule_frame = tk.Frame(self)
        self.sort_rule_frame.pack(anchor='w')
        for filter in card_filters:
            self.add_filter_rule(filter['name'], filter['function'])

        self.add_sort_button = tk.Button(self, text='+ Custom', height=2, width=10, command=self.add_custom_sort, bg='blue')
        self.add_sort_button.pack(anchor='w')

    def add_filter_rule(self, filter_name, filter_function):
        filter_var = tk.BooleanVar()
        checkbutton = tk.Checkbutton(self.sort_rule_frame, text=filter_name, variable=filter_var, command=self.filter_and_sort_callback)
        checkbutton.pack(anchor='w')
        self.sort_vars[filter_name] = filter_var
        self.individual_card_sort_functions[filter_name] = filter_function

    def add_custom_sort(self):
        rule_var = tk.StringVar()
        custom_sort_window = CustomSortWindow(self, rule_var)
        self.wait_window(custom_sort_window)
        print(f"Created rule: {rule_var.get()}")
        if not validate_filter(rule_var.get()):
            print('Invalid filter')
            return
        self.add_filter_rule(rule_var.get(), rule_var.get())
        new_filter = save_new_filter(self.deck_collection.get_user(), rule_var.get(), rule_var.get())
        self.individual_card_sort_functions[rule_var.get()] = new_filter['function']

    def sort_by_custom_card_filter(self, decks, filter):
        sorted_decks = []
        for deck in decks:
            public_id = deck.get('publicId', '')
            count = self.deck_collection.count_cards_with_property(public_id, filter)
            sorted_decks.append((deck, count))

        sorted_decks.sort(key=lambda x: x[1], reverse=True)
        return sorted_decks

    def sort_decks(self, decks):
        if self.is_sorting_enabled():
            custom_sort_name = self.get_first_checked_sort()
            sorted_decks = self.sort_by_custom_card_filter(decks, self.individual_card_sort_functions[custom_sort_name])
            return sorted_decks
        else:
            return decks

    def is_sorting_enabled(self):
        return self.get_first_checked_sort() is not None
    
    def get_first_checked_sort(self):
        for sort_var_name in self.sort_vars.keys():
            if self.sort_vars[sort_var_name].get():
                return sort_var_name
        return None