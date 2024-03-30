import tkinter as tk
from PIL import Image, ImageTk

class DeckQueue(tk.Canvas):
    def __init__(self, root, deck, deck_list):
        super().__init__(root)
        self.root = root
        self.deck = deck
        self.deck_list = deck_list
        self.deck_index = self.deck_list.index(self.deck)

        self.create_deck_queue()

    def create_deck_queue(self):
        deck_queue_frame = tk.Frame(self)
        self.create_window((0, 0), window=deck_queue_frame, anchor='nw')

        for deck_in_list in self.deck_list:
            image_path = deck_in_list.get('local_image_path', 'resources\\no-photo.png')

            # Load image and resize it to desired dimensions
            image = Image.open(image_path)
            image = image.resize((126, 176))
            photo = ImageTk.PhotoImage(image)

            deck_image_label = tk.Label(deck_queue_frame, image=photo)
            deck_image_label.pack(side=tk.TOP)

            # Save a reference to avoid garbage collection
            deck_image_label.image = photo
