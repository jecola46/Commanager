import tkinter as tk
from deck_collection import DeckCollection
from ui_elements.deck_lister import DeckLister
from deck_io import grab_decks_from_moxfield, load_decks_from_file, save_decks_to_file

class MainAppUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MTG Deck Manager")

        self.deck_collection = DeckCollection()

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Enter your Moxfield username:")
        label.pack(pady=10)

        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=10)

        grab_button = tk.Button(self, text="Grab Decks", command=self.grab_decks)
        grab_button.pack(pady=10)

        save_button = tk.Button(self, text="Save Decks to File", command=self.save_decks)
        save_button.pack(pady=10)

        load_button = tk.Button(self, text="Load Decks from File", command=self.load_decks)
        load_button.pack(pady=10)

        list_decks_button = tk.Button(self, text="List Decks", command=self.list_decks)
        list_decks_button.pack(pady=10)

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
        missing_shocks_button.pack(pady=10)

        missing_command_tower_button = tk.Button(self, text="Find Decks with missing command towers", command=self.find_missing_command_towers)
        missing_command_tower_button.pack(pady=10)

    def find_missing_shocks(self):
        decks_color_dict = self.deck_collection.get_deck_colors_map()
        decks_with_missing = []
        for deck_id in decks_color_dict:
            colors = decks_color_dict[deck_id]
            if "W" in colors and "U" in colors:
                if self.deck_collection.deck_does_not_have(deck_id, "Hallowed Fountain"):
                    decks_with_missing.append(deck_id)
                    continue
            if "W" in colors and "B" in colors:
                if self.deck_collection.deck_does_not_have(deck_id, "Godless Shrine"):
                    decks_with_missing.append(deck_id)
                    continue
            if "W" in colors and "R" in colors:
                if self.deck_collection.deck_does_not_have(deck_id, "Sacred Foundry"):
                    decks_with_missing.append(deck_id)
                    continue
            if "W" in colors and "G" in colors:
                if self.deck_collection.deck_does_not_have(deck_id, "Temple Garden"):
                    decks_with_missing.append(deck_id)
                    continue
            if "U" in colors and "B" in colors:
                if self.deck_collection.deck_does_not_have(deck_id, "Watery Grave"):
                    decks_with_missing.append(deck_id)
                    continue
            if "U" in colors and "R" in colors:
                if self.deck_collection.deck_does_not_have(deck_id, "Steam Vents"):
                    decks_with_missing.append(deck_id)
                    continue
            if "U" in colors and "G" in colors:
                if self.deck_collection.deck_does_not_have(deck_id, "Breeding Pool"):
                    decks_with_missing.append(deck_id)
                    continue
            if "B" in colors and "R" in colors:
                if self.deck_collection.deck_does_not_have(deck_id, "Blood Crypt"):
                    decks_with_missing.append(deck_id)
                    continue
            if "B" in colors and "G" in colors:
                if self.deck_collection.deck_does_not_have(deck_id, "Overgrown Tomb"):
                    decks_with_missing.append(deck_id)
                    continue
            if "R" in colors and "G" in colors:
                if self.deck_collection.deck_does_not_have(deck_id, "Stomping Ground"):
                    decks_with_missing.append(deck_id)
                    continue

        self.deck_lister.highlight_decks(decks_with_missing)

    def find_missing_command_towers(self):
        decks_color_dict = self.deck_collection.get_deck_colors_map()
        decks_with_missing = []
        for deck_id in decks_color_dict:
            colors = decks_color_dict[deck_id]
            if len(colors) > 1:
                if self.deck_collection.deck_does_not_have(deck_id, "Command Tower"):
                    decks_with_missing.append(deck_id)

        self.deck_lister.highlight_decks(decks_with_missing)

if __name__ == "__main__":
    app_ui = MainAppUI()
    app_ui.mainloop()