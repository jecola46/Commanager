import tkinter as tk
from PIL import Image, ImageTk
from deck_io import grab_card_art_async

class DeckLister(tk.Canvas):
    def __init__(self, root, deck_lists, deck_collection):
        super().__init__(root)
        self.root = root
        self.root.title("Deck Viewer")
        self.deck_lists = deck_lists
        self.deck_collection = deck_collection

        self.create_deck_collection()

    def create_deck_collection(self):
        self.deck_image_labels = []
        
        self.bind_all("<MouseWheel>", self.on_mousewheel)
        self.set_scrollbar()

        # Create a frame to contain the deck boxes
        deck_collection_frame = tk.Frame(self)
        self.create_window((0, 0), window=deck_collection_frame, anchor='nw')

        self.grid_rowconfigure(1, weight=1)

        for column in range(0, 7):
            deck_collection_frame.grid_columnconfigure(column, weight=1, uniform="group1")

        # Create a grid for displaying decks
        for i, deck in enumerate(self.deck_lists):
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
            deck_name_label.pack(side = tk.TOP, padx=2)

        grab_card_art_async(self.deck_image_labels)

    def set_scrollbar(self):
        # Bind scrollbar to canvas
        self.bind("<Configure>", self.on_canvas_configure)

    def on_canvas_configure(self, event):
        self.configure(scrollregion=self.bbox("all"))

    def on_mousewheel(self, event):
        self.yview_scroll(-1 * int(event.delta/120), "units")