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
        deck_list_label = tk.Label(self, text="Your decks", font=("Helvetica", 24))
        deck_list_label.grid(row=0, column=1, pady=10, sticky='ew')

        self.grid_columnconfigure(1, weight=1)

        self.deck_image_labels = []

        # Create a canvas for scrollable area
        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=1, column=1, sticky='nsew')
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        # Add a scrollbar
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        scrollbar.grid(row=1, column=2, sticky='ns')
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame to contain the deck boxes
        deck_collection_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=deck_collection_frame, anchor='nw')

        # Bind scrollbar to canvas
        def on_canvas_configure(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        # Bind scrollbar to canvas
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.grid_rowconfigure(1, weight=1)

        for column in range(0, 7):
            deck_collection_frame.grid_columnconfigure(column, weight=1, uniform="group1")

        # Create a grid for displaying decks
        for i, deck in enumerate(self.deck_collection.get_deck_summaries()):
            image_path = deck.get('local_image_path', 'resources\\no-photo.png')

            # Calculate row and column index
            row = i // 7
            column = i % 7

            # Load image and resize it to desired dimensions
            image = Image.open(image_path)
            image = image.resize((212, 156))
            photo = ImageTk.PhotoImage(image)

            deck_box_frame = tk.Frame(deck_collection_frame)
            deck_box_frame.grid(row=row, column=column, padx=10, pady=5)

            # Create label to display image
            deck_image_label = tk.Label(deck_box_frame, image=photo)
            deck_image_label.card_art_name = self.deck_collection.get_deck_commander_name(deck['publicId'])
            deck_image_label.image = photo  # Keep reference to avoid garbage collection
            deck_image_label.pack(side = tk.TOP, padx=5)
            self.deck_image_labels.append(deck_image_label)

            # Display deck name
            deck_name = deck.get('name', 'Unknown Deck').replace('[Owned]', '')
            # Shorten long deck names
            deck_name = (deck_name[:36] + '...') if len(deck_name) > 39 else deck_name

            deck_name_label = tk.Label(deck_box_frame, text=deck_name, font=("Helvetica", 12))
            deck_name_label.pack(side = tk.TOP, padx=5)

        grab_card_art_async(self.deck_image_labels)

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * int(event.delta/120), "units")