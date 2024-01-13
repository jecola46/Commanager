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