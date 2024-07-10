import tkinter as tk
from tkinter import ttk
from .deck_manager_app import DeckManagerApp
from deck_io import grab_decks_from_moxfield, load_decks_from_file
from deck_collection import DeckCollection

class CollectionLoader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MTG Deck Manager")
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure((0, 2), weight=1, uniform="group1")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)

        # Welcome text
        welcome_label = tk.Label(self, text="Welcome to the Really Great MTG Tool", font=("Helvetica", 16)) 
        welcome_label.grid(row=0, column=0, columnspan=3, pady=10, sticky='ew')

        # Parent frame for username entry, centers contents in column
        username_parent_frame = tk.Frame(self)
        username_parent_frame.grid(row=1, column=0, padx=10, sticky='ew')

        # Child frame for username entry, packs contents together into small frame
        username_entry_frame = tk.Frame(username_parent_frame)
        username_entry_frame.pack(anchor=tk.CENTER)

        # Moxfield username entry
        username_label = tk.Label(username_entry_frame, text="Enter your Moxfield username:")
        username_label.pack(side = tk.LEFT)
        self.username_entry = tk.Entry(username_entry_frame)
        self.username_entry.pack(side = tk.LEFT, padx=10)

        fetch_button = tk.Button(username_entry_frame, text="Submit", command=self.fetch_deck_info)
        fetch_button.pack(side = tk.LEFT)
        self.bind('<Return>', self.fetch_deck_info)  # let the user submit on pressing the `Enter` key

        ttk.Separator(self, orient='vertical').grid(column=1, row=1, rowspan=3, sticky='ns', pady=(0, 10))

        # "or" text written on top of the separator
        divider_label = tk.Label(self, text="or")
        divider_label.grid(row=1, column=1, rowspan=2, padx=10, pady=10)

        # Button to load decks from a known file
        load_file_button = tk.Button(self, text="Load Decks from File", command=self.load_decks_from_default_file, bg='light blue')
        load_file_button.grid(row=1, column=2, padx=40, pady=40, sticky='nsew')

    def fetch_deck_info(self, event=None):
        # bind(), used to register the `Enter` keypress, passes in `event` as an argument to the callback`. 
        # However, Button(), the UI button, does not. So, we're just accounting for both cases
        username = self.username_entry.get()

        update_loading_callback = self.show_loading_screen("Fetching deck information...")

        # Fetch deck information
        deck_summaries, deck_details = grab_decks_from_moxfield(username, update_loading_callback)

        self.replace_with_main_app(deck_summaries, deck_details)

    def show_loading_screen(self, text):
        # Create a transparent overlay
        self.loading_overlay = tk.Canvas(self, bg="grey", highlightthickness=0, bd=0, relief="ridge")
        self.loading_overlay.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.loading_label = tk.Label(self, bg="grey", text=text, font=("Helvetica", 12), fg="blue")
        self.loading_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create progress bar
        self.progress_bar = ttk.Progressbar(self, mode='determinate')
        self.progress_bar.place(relx=0.5, rely=0.6, relwidth=0.5, anchor=tk.CENTER)
        self.update_idletasks()  # Update the GUI to show the label immediately
        def update_label(new_text, new_progress):
            self.loading_label.config(text=new_text)
            self.loading_label.update()
            self.progress_bar.step(new_progress)
            self.progress_bar.update()
        return update_label

    def load_decks_from_default_file(self):
        username = self.username_entry.get()  
        # This will be None in most cases, in which the first directory in user_data found will be chosen to read from
        # COMM-22: instead of `self.username_entry.get()`, read from the most_recent_user file!!
        # COMM-24: give user a dropdown of saved users and then use the selected username
        
        self.replace_with_main_app(*load_decks_from_file(username))

    def replace_with_main_app(self, deck_summaries, deck_details):
        deck_collection = DeckCollection()
        deck_collection.set_deck_summaries(deck_summaries)
        deck_collection.set_deck_details(deck_details)

        # Destroy current frame
        self.destroy()

        deck_manager_app = DeckManagerApp(deck_collection)
        deck_manager_app.minsize(600, 600)
        deck_manager_app.geometry('1800x600')
        deck_manager_app.mainloop()

        self.should_restart = deck_manager_app.should_restart if hasattr(deck_manager_app, 'should_restart') else False