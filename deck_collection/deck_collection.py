import json

class DeckCollection:
    def __init__(self):
        self.deck_summaries = []
        self.deck_details = {}

    def set_deck_summaries(self, deck_summaries):
        self.deck_summaries = deck_summaries

    def get_deck_summaries(self):
        return self.deck_summaries

    def set_deck_details(self, deck_details):
        with open("./user_data/cards.json", "r", encoding="utf-8") as file:
            card_list = json.load(file)

        # Function to find a card by name
        def find_card_by_name(name, card_list):
            for card in card_list:
                if card.get("name") == name:
                    return card
            print(f"Could not find {name}")
            return None

        end_collection = {}
        for publicId, deck in deck_details.items():
            mainboard = {}
            cards = deck['list']
            for card in cards:
                start = card.find(" ") + 1
                end = card.find("(") - 1
                card = card[start:end]
                card_name = find_card_by_name(card, card_list)
                if card_name is None:
                    print(f"In list {publicId}")
                mainboard[card] = card_name
            end_collection[publicId] = deck
            end_collection[publicId]["mainboard"] = mainboard

        self.deck_details = deck_details

    def get_deck_details(self):
        return self.deck_details

    def get_deck_colors_map(self):
        """
        Returns a map from deck id to deck colors.

        Returns:
        - dict: A dictionary mapping deck id to deck colors.
        """
        return dict(map(lambda deck_summary: (deck_summary.get('publicId', ''), deck_summary.get('colors', [])), self.deck_summaries))

    def deck_does_not_have(self, deck_id, card_name):
        return card_name not in self.deck_details[deck_id]['mainboard']

    def get_deck_description(self, deck_id):
        return self.deck_details[deck_id]['description']

    def get_deck_commander_name(self, deck_id):
        return list(self.deck_details[deck_id]['commanders'].keys())[0]

    def get_deck_description(self, deck_id):
        return self.deck_details[deck_id]['description']

    def get_card_stats(self):
        cards = {}
        for deck_id in self.deck_details:
            deck_list = self.deck_details[deck_id]['mainboard']
            for card_name in deck_list:
                if card_name in cards:
                    cards[card_name] += deck_list[card_name]['quantity']
                else:
                    cards[card_name] = deck_list[card_name]['quantity']

        card_tuples = list(cards.items())
        sorted_card_tuples = sorted(card_tuples, key=lambda x: x[1], reverse=True)

        return sorted_card_tuples

    def sort_decks_by_property(self, card_property_lambda):
        sorted_decks = []
        for deck_id, deck_list in self.deck_details.items():
            count = sum(1 for card_name, card_info in deck_list['mainboard'].items() if card_property_lambda(card_info))
            sorted_decks.append((deck_list['name'], count))

        sorted_decks.sort(key=lambda x: x[1], reverse=True)
        return sorted_decks

    def count_cards_with_property(self, public_id, card_property_lambda):
        for card_name, card_info in self.deck_details[public_id]['mainboard'].items():
            card_property_lambda(card_info)
        return sum(1 for card_name, card_info in self.deck_details[public_id]['mainboard'].items() if card_property_lambda(card_info))

    def get_friendly_name_for_deck(self, deck, prefix=None):
        # Display deck name
        deck_name = deck.get('name', 'Unknown Deck').replace('[Owned]', '')
        if prefix is not None:
            # Add Prefix
            deck_name = f'{prefix} {deck_name}'
        # Shorten long deck names
        return (deck_name[:36] + '...') if len(deck_name) > 39 else deck_name

    def get_cards_in_deck(self, deck_id):
        return self.deck_details[deck_id]['mainboard']
    
    def get_user(self):
        return self.deck_summaries[0]['createdByUser']['userName']