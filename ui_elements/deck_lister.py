import tkinter as tk
from .deck_viewer import DeckViewer

class DeckLister(tk.Frame):
    def __init__(self, root, deck_collection):
        super().__init__(root, None)
        self.root = root
        self.root.title("Deck Viewer")
        self.deck_collection = deck_collection

        self.create_deck_listbox()
        

    def create_deck_listbox(self):
        # Create a listbox to display decks
        self.deck_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE, height=65, width=80)
        self.deck_listbox.grid(row=1, column=2, pady=10, sticky='w', rowspan=5)

        # Populate the listbox with deck names
        self.populate_deck_list()

        # Bind the listbox selection to display deck details
        self.deck_listbox.bind('<<ListboxSelect>>', self.display_deck_details)

    def populate_deck_list(self):
        # Clear existing items in the listbox
        self.deck_listbox.delete(0, tk.END)

        # Get the deck names from the collection
        decks = self.deck_collection.get_deck_summaries()
        self.decks = []

        # Populate the listbox with deck names
        for deck in decks:
            self.deck_listbox.insert(tk.END, deck['name'])
            self.decks.append(deck)

    def display_deck_details(self, event):
        deck = self.decks[self.deck_listbox.curselection()[0]]
        self.show_deck_viewer(deck)
        print(deck)

    def show_deck_viewer(self, deck):
        self.destroy_widgets()

        # Create and place the DeckViewer instance
        deck_viewer = DeckViewer(self.root, self.deck_collection, deck, self.back_to_deck_lister)
        deck_viewer.grid(row=1, column=2, pady=10, sticky='w', rowspan=5)

    def back_to_deck_lister(self):
        self.create_deck_listbox()

    def destroy_widgets(self):
        self.deck_listbox.destroy()

    def highlight_decks(self, decks):
        for x in range(len(self.decks)):
            deck = self.decks[x]
            if deck['publicId'] in decks:
                self.deck_listbox.select_set(x)

    def list_decks_with_num(self, decks_and_count):
        # Clear existing items in the listbox
        self.deck_listbox.delete(0, tk.END)
        self.decks = []

        # Populate the listbox with deck names
        for deck, count in decks_and_count:
            self.deck_listbox.insert(tk.END, deck + f' {count}')
            self.decks.append(deck)
