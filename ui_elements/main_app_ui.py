import tkinter as tk
from PIL import Image, ImageTk
import math
from deck_io import grab_card_art_async

class MainAppUI(tk.Tk):
    def __init__(self, deck_collection):
        super().__init__()
        self.title("MTG Deck Manager")

        self.deck_collection = deck_collection

        self.create_widgets()

    def create_widgets(self):
        for column in range(1, 8):
            self.grid_columnconfigure(column, weight=1, uniform="group1")
        deck_list_label = tk.Label(self, text="Your decks", font=("Helvetica", 24))
        deck_list_label.grid(row=0, column=1, columnspan=7, pady=10, sticky='ew')

        self.deck_image_labels = []

        # Create a grid for displaying decks
        for i, deck in enumerate(self.deck_collection.get_deck_summaries()):
            image_path = deck.get('local_image_path', 'resources\\no-photo.png')

            # Calculate row and column index
            row = math.floor(i / 7) + 1
            column = math.floor(i % 7) + 1

            # Load image and resize it to desired dimensions
            image = Image.open(image_path)
            image = image.resize((212, 156))
            photo = ImageTk.PhotoImage(image)

            deck_box_frame = tk.Frame(self)
            deck_box_frame.grid(row=row, column=column, padx=10, pady=5)

            # Create label to display image
            deck_image_label = tk.Label(deck_box_frame, image=photo)
            deck_image_label.card_art_name = self.deck_collection.get_deck_commander_name(deck['publicId'])
            deck_image_label.image = photo  # Keep reference to avoid garbage collection
            deck_image_label.pack(side = tk.TOP, padx=10)
            self.deck_image_labels.append(deck_image_label)

            # Display deck name
            deck_name = deck.get('name', 'Unknown Deck').replace('[Owned]', '')
            # Shorten long deck names
            deck_name = (deck_name[:36] + '...') if len(deck_name) > 39 else deck_name

            deck_name_label = tk.Label(deck_box_frame, text=deck_name, font=("Helvetica", 12))
            deck_name_label.pack(side = tk.TOP, padx=10)

        grab_card_art_async(self.deck_image_labels)