import tkinter as tk
from .collection_screen import CollectionScreen

class DeckManagerApp(tk.Tk):
    def __init__(self, deck_collection):
        super().__init__()
        self.title("MTG Deck Manager")

        self.deck_collection = deck_collection

        self.create_main_frame()

    def create_main_frame(self):
        self.main_frame = CollectionScreen(self, self.deck_collection)
        self.main_frame.pack(fill="both", expand=True)

    def show_deck_details_screen(self, deck):
        self.main_frame.destroy()  # Destroy the current main frame
        self.create_deck_details_frame(deck)  # Create the deck details frame

    def create_deck_details_frame(self, deck):
        self.deck_details_frame = DeckDetailsScreen(self, deck)
        self.deck_details_frame.pack(fill="both", expand=True)