import tkinter as tk

class CardStats(tk.Frame):
    def __init__(self, root, deck_collection):
        super().__init__(root, None)
        self.root = root
        self.root.title("Card Stats")
        self.deck_collection = deck_collection

        # Create a listbox to display card stats
        self.card_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=65, width=80)
        self.card_listbox.grid(row=1, column=2, pady=10, sticky='w', rowspan=5)

        # Populate the listbox with deck names
        self.populate_card_stats()

        # Bind the listbox selection to display deck details
        self.card_listbox.bind('<<ListboxSelect>>', self.display_card_details)

    def populate_card_stats(self):
        # Clear existing items in the listbox
        self.card_listbox.delete(0, tk.END)

        # Get the card names from the collection
        cards = self.deck_collection.get_card_stats()
        self.cards = []

        inserted_count = 0
        # Populate the listbox with card stats
        for card in cards:
            if inserted_count > 60:
                break
            self.card_listbox.insert(tk.END, f'{card[0]}: {card[1]}')
            self.cards.append(card)
            inserted_count += 1

    def display_card_details(self, event):
        card = self.cards[self.card_listbox.curselection()[0]]
        print(card)

    def destroy_widgets(self):
        self.card_listbox.destroy()