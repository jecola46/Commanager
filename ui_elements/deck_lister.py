import tkinter as tk
from PIL import Image, ImageTk
from deck_io import grab_card_art_async

class DeckLister(tk.Canvas):
    def __init__(self, root, deck_lists, deck_collection):
        super().__init__(root)
        self.root = root
        self.deck_lists = deck_lists
        self.deck_collection = deck_collection

        self.create_deck_collection()

    def create_deck_collection(self):
        num_columns = 5

        self.deck_image_labels = []
        
        self.bind_all("<MouseWheel>", self.on_mousewheel)

        # Create a frame to contain the deck boxes
        deck_collection_frame = tk.Frame(self)
        self.create_window((0, 0), window=deck_collection_frame, anchor='nw')

        self.grid_rowconfigure(1, weight=1)

        for column in range(0, num_columns):
            deck_collection_frame.grid_columnconfigure(column, weight=1, uniform="group1")

        # Create a grid for displaying decks
        for i, deck in enumerate(self.deck_lists):
            image_path = deck.get('local_image_path', 'resources\\no-photo.png')

            # Calculate row and column index
            row = i // num_columns
            column = i % num_columns

            # Load image and resize it to desired dimensions
            image = Image.open(image_path)
            image = image.resize((212, 156))
            photo = ImageTk.PhotoImage(image)

            deck_box_frame = tk.Frame(deck_collection_frame)
            deck_box_frame.grid(row=row, column=column, pady=5)

            # Create label to display image
            deck_image_label = tk.Label(deck_box_frame, image=photo)
            deck_image_label.card_art_name = self.deck_collection.get_deck_commander_name(deck['publicId'])
            deck_image_label.image = photo  # Keep reference to avoid garbage collection
            deck_image_label.pack(side = tk.TOP, padx=50)
            self.deck_image_labels.append(deck_image_label)

            deck_name = self.deck_collection.get_friendly_name_for_deck(deck)

            deck_name_label = tk.Label(deck_box_frame, text=deck_name, font=("Helvetica", 12))
            deck_name_label.pack(side = tk.TOP, padx=2)

            deck_image_label.bind("<Button-1>", lambda event, deck=deck: self.root.show_deck_details(deck))


        self.set_scrollbar()
        grab_card_art_async(self.deck_image_labels)

    def set_scrollbar(self):
        # Bind scrollbar to canvas
        self.bind("<Configure>", self.on_canvas_configure)

    def on_canvas_configure(self, event):
        self.configure(scrollregion=self.bbox("all"))

    def on_mousewheel(self, event):
        # Get the dimensions of the canvas viewport
        canvas_height = self.winfo_height()

        # Get the dimensions of the scroll region
        scroll_region = self.bbox("all")
        scroll_height = scroll_region[3] - scroll_region[1]

        if scroll_height > canvas_height:
            self.yview_scroll(-1 * int(event.delta/120), "units")

    def update_things(self):
        self.configure(scrollregion=self.bbox("all"))