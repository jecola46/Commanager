import tkinter as tk
from tkinter import ttk
from .main_app_ui import MainAppUI
from deck_io import grab_decks_from_moxfield, load_decks_from_file
from deck_collection import DeckCollection

class CollectionLoader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MTG Deck Manager")

        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform="group1")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)

        # Welcome text
        welcome_label = tk.Label(self, text="Welcome to the Really Great MTG Tool", font=("Helvetica", 16))
        welcome_label.grid(row=0, column=0, columnspan=7, pady=10, sticky='ew')

        # Moxfield username entry
        username_label = tk.Label(self, text="Enter your Moxfield username:")
        username_label.grid(row=1, column=0, sticky='we', padx=10, pady=10)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=1, column=1, sticky='we', padx=10, pady=10)

        # Moxfield username entry and submit button
        username_label = tk.Label(self, text="Enter your Moxfield username:")
        username_label.grid(row=1, column=0, sticky='we', padx=10, pady=10)

        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=1, column=1, sticky='we', padx=10, pady=10)
        fetch_button = tk.Button(self, text="Submit", command=self.fetch_deck_info)
        fetch_button.grid(row=1, column=2, padx=10, pady=10)

        ttk.Separator(self, orient='vertical').grid(column=3, row=1, rowspan=3, sticky='ns')

        # Divider with "or"
        divider_label = tk.Label(self, text="or")
        divider_label.grid(row=1, column=3, rowspan=2, padx=10, pady=10)

        # Button to load decks from a known file
        load_file_button = tk.Button(self, text="Load Decks from File", command=self.load_decks_from_default_file)
        load_file_button.grid(row=1, column=4, columnspan=3, padx=10, pady=10, sticky='nsew')


    def fetch_deck_info(self):
        # Functionality to fetch deck information
        username = self.username_entry.get()

        self.replace_with_main_app(*grab_decks_from_moxfield(username))

    def load_decks_from_default_file(self):
        self.replace_with_main_app(*load_decks_from_file())

    def replace_with_main_app(self, deck_summaries, deck_details):
        deck_collection = DeckCollection()
        deck_collection.set_deck_summaries(deck_summaries)
        deck_collection.set_deck_details(deck_details)

        # Functionality to load decks from a known file
        # Destroy current frame
        self.destroy()

        # Create and display MainAppUI
        main_app = MainAppUI(deck_collection)
        main_app.mainloop()