import tkinter as tk
from PIL import Image, ImageTk
from deck_io import grab_card_art_async

class DeckQueue(tk.Canvas):
    def __init__(self, root, deck_collection, deck, deck_lists):
        super().__init__(root)
        self.root = root
        self.deck_collection = deck_collection
        self.deck = deck
        self.deck_lists = deck_lists
        self.deck_index = self.deck_lists.index(self.deck)

        self.create_deck_queue()

    def create_deck_queue(self):
        deck_queue_frame = tk.Frame(self)
        self.create_window((0, 0), window=deck_queue_frame, anchor='nw')

        self.deck_image_labels = []

        # Get decks around the chosen deck
        num_decks = len(self.deck_lists)
        start_index = max(0, self.deck_index - 2)
        end_index = min(num_decks, self.deck_index + 3)

        # Adjust start_index and end_index if there are fewer than 5 decks
        if end_index - start_index < 5:
            if start_index == 0:
                end_index = min(num_decks, start_index + 5)
            elif end_index == num_decks:
                start_index = max(0, end_index - 5)

        for i in range(start_index, end_index):
            deck_in_list = self.deck_lists[i]
            image_path = deck_in_list.get('local_image_path', 'resources\\no-photo.png')

            # Load image and resize it to desired dimensions
            image = Image.open(image_path)
            image = image.resize((126, 176))
            photo = ImageTk.PhotoImage(image)

            deck_image_label = tk.Label(deck_queue_frame, image=photo)
            if i == self.deck_index:
                deck_image_label.config(bg= "blue")
            
            deck_image_label.card_art_name = self.deck_collection.get_deck_commander_name(deck_in_list['publicId'])
            deck_image_label.image = photo
            deck_image_label.pack(side=tk.TOP)

            self.deck_image_labels.append(deck_image_label)

            # Save a reference to avoid garbage collection
            deck_image_label.image = photo

        grab_card_art_async(self.deck_image_labels, resize=(212, 156))