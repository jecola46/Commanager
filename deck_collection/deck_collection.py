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