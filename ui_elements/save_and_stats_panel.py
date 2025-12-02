import tkinter as tk
from deck_io import save_decks_to_file

class SaveAndStatsPanel(tk.Frame):
    def __init__(self, root, deck_collection):
        super().__init__(root)
        self.root = root
        self.deck_collection = deck_collection
        self.create_save_and_stats_ui()

    def create_save_and_stats_ui(self):
        self.collection_analysis_button = tk.Button(self, text='Collection Analysis', height=4, width=15, command=self.show_collection_analysis, bg='blue')
        self.collection_analysis_button.pack(side=tk.TOP, pady=5)

        self.swap_user_button = tk.Button(self, text='Swap User Data', height=4, width=15, command=self.save_and_swap_collection, bg='red')
        self.swap_user_button.pack(side=tk.TOP, pady=5)

    def save_and_swap_collection(self):
        save_decks_to_file(self.deck_collection.get_deck_summaries(), self.deck_collection.get_deck_details())
        self.root.return_to_deck_loader()

    def show_collection_analysis(self):
        self.root.show_collection_analysis_screen()
