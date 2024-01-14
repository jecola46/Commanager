import tkinter as tk
from deck_collection import DeckCollection
from ui_elements.deck_lister import DeckLister
from deck_io import grab_decks_from_moxfield, load_decks_from_file, save_decks_to_file
from deck_analysis_utils import is_missing_command_tower, is_missing_shock

class MainAppUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MTG Deck Manager")

        self.deck_collection = DeckCollection()

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Enter your Moxfield username:")
        label.grid(row=0, column=0, pady=10, sticky='w')

        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, pady=10, sticky='w')

        grab_button = tk.Button(self, text="Grab Decks", command=self.grab_decks)
        grab_button.grid(row=1, column=0, pady=10, sticky='w')

        save_button = tk.Button(self, text="Save Decks to File", command=self.save_decks)
        save_button.grid(row=2, column=0, pady=10, sticky='w')

        load_button = tk.Button(self, text="Load Decks from File", command=self.load_decks)
        load_button.grid(row=3, column=0, pady=10, sticky='w')

        list_decks_button = tk.Button(self, text="List Decks", command=self.list_decks)
        list_decks_button.grid(row=4, column=0, pady=10, sticky='w')

        # Create the deck lister on the right side
        self.deck_lister = DeckLister(self, self.deck_collection)
        self.deck_lister.grid(row=0, column=2, rowspan=5, padx=10, pady=10, sticky='nsew')

        # Configure row and column weights for resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(2, weight=2)  # Adjust the weight based on your preference

    def grab_decks(self):
        deck_summaries, deck_details = grab_decks_from_moxfield(self.username_entry.get())
        self.deck_collection.set_deck_summaries(deck_summaries)
        self.deck_collection.set_deck_details(deck_details)

    def save_decks(self):
        save_decks_to_file(self.deck_collection.get_deck_summaries(), self.deck_collection.get_deck_details())

    def load_decks(self):
        deck_summaries, deck_details = load_decks_from_file()
        self.deck_collection.set_deck_summaries(deck_summaries)
        self.deck_collection.set_deck_details(deck_details)

    def list_decks(self):
        self.deck_lister = DeckLister(self, self.deck_collection)
        missing_shocks_button = tk.Button(self, text="Find Decks with missing shocks", command=self.find_missing_shocks)
        missing_shocks_button.grid(row=5, column=0, pady=10, sticky='w')

        missing_command_tower_button = tk.Button(self, text="Find Decks with missing command towers", command=self.find_missing_command_towers)
        missing_command_tower_button.grid(row=6, column=0, pady=10, sticky='w')

    def find_missing_shocks(self):
        decks_color_dict = self.deck_collection.get_deck_colors_map()
        decks_with_missing = []
        for deck_id in decks_color_dict:
            colors = decks_color_dict[deck_id]
            if is_missing_shock(self.deck_collection, deck_id, colors):
                decks_with_missing.append(deck_id)

        self.deck_lister.highlight_decks(decks_with_missing)

    def find_missing_command_towers(self):
        decks_color_dict = self.deck_collection.get_deck_colors_map()
        decks_with_missing = []
        for deck_id in decks_color_dict:
            colors = decks_color_dict[deck_id]
            if is_missing_command_tower(self.deck_collection, deck_id, colors):
                decks_with_missing.append(deck_id)

        self.deck_lister.highlight_decks(decks_with_missing)

if __name__ == "__main__":
    app_ui = MainAppUI()
    app_ui.mainloop()