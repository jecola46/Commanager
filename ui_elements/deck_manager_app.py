import tkinter as tk
from .collection_screen import CollectionScreen
from .deck_details_screen import DeckDetailsScreen

class DeckManagerApp(tk.Tk):
    def __init__(self, deck_collection):
        super().__init__()
        self.title("MTG Deck Manager")

        self.deck_collection = deck_collection

        self.create_main_frame()

    def create_main_frame(self):
        self.collection_frame = CollectionScreen(self, self.deck_collection)
        self.collection_frame.pack(fill="both", expand=True)

    def show_deck_details_screen(self, deck, deck_lists):
        self.collection_frame.pack_forget()
        self.create_deck_details_frame(deck, deck_lists)

    def create_deck_details_frame(self, deck, deck_lists):
        self.deck_details_frame = DeckDetailsScreen(self, self.deck_collection, deck, deck_lists)
        self.deck_details_frame.pack(fill="both", expand=True)

    def show_main_frame(self):
        self.deck_details_frame.destroy()
        self.collection_frame.pack(fill="both", expand=True)