import tkinter as tk
from PIL import Image, ImageTk
from deck_io import grab_card_image_async
from .deck_queue import DeckQueue

class DeckDetailsScreen(tk.Frame):
    def __init__(self, root, deck_collection, deck, deck_list):
        super().__init__(root)
        self.root = root
        self.deck_collection = deck_collection
        self.deck = deck
        self.deck_list = deck_list
        self.deck_index = self.deck_list.index(self.deck)

        self.create_widgets()

    def create_widgets(self):
        home_button = tk.Button(self, text='Home', command=self.return_home)
        home_button.grid(row=0, column=0, pady=10)

        deck_name = self.deck_collection.get_friendly_name_for_deck(self.deck)

        deck_name_label = tk.Label(self, text=deck_name, font=("Helvetica", 24))
        deck_name_label.grid(row=0, column=1, pady=10, sticky='ew')

        self.card_image_labels = []
        image_path = self.deck.get('local_card_image_path', 'resources\\no-photo.png')

        # Load image and resize it to desired dimensions
        image = Image.open(image_path)
        image = image.resize((630, 880))
        photo = ImageTk.PhotoImage(image)

        # Create label to display image
        card_image_label = tk.Label(self, image=photo)
        card_image_label.card_name = self.deck_collection.get_deck_commander_name(self.deck['publicId'])
        card_image_label.grid(row=1, column=1, pady=10)

        self.card_image_labels.append(card_image_label)

        grab_card_image_async(self.card_image_labels)

        progression_button_frame = tk.Frame(self)
        progression_button_frame.grid(row=2, column=1, pady=10, sticky='ew')

        previous_button = tk.Button(progression_button_frame, text='Previous', height=2, width=10, command=self.previous_deck)
        if self.deck_index == 0:
            previous_button['state'] = tk.DISABLED
        previous_button.config(font = ("Helvetica", 20))
        previous_button.pack(side=tk.LEFT, padx='10')

        next_button = tk.Button(progression_button_frame, text='Next', height=2, width=10, command=self.next_deck)
        if self.deck_index == len(self.deck_list) - 1:
            next_button['state'] = tk.DISABLED
        next_button.config(font = ("Helvetica", 20))
        next_button.pack(side=tk.RIGHT, padx='10')

        deck_queue = DeckQueue(self, self.deck_collection, self.deck, self.deck_list)
        deck_queue.grid(row=1, column=0, sticky='nsew')

    def previous_deck(self):
        self.root.show_new_deck(self.deck_list[self.deck_index - 1], self.deck_list)

    def next_deck(self):
        self.root.show_new_deck(self.deck_list[self.deck_index + 1], self.deck_list)

    def return_home(self):
        self.root.show_main_frame()