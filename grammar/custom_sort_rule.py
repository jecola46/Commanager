from enum import StrEnum
from .rule_part import RulePart
from .string_comparision import StringComparision
from .numerical_comparision import NumericalComparision

class SortRuleType(StrEnum):
        NOT_ENTERED = "-"
        TYPE_LINE = "Type line"
        MANA_VALUE = "Mana value is"
        ORACLE_TEXT = "Oracle text"
        POWER = "Power is"
        TOUGHNESS = "Toughness is"

current_to_next_class_map = {
    "-": None,
    "Type line": StringComparision,
    "Mana value is": NumericalComparision,
    "Oracle text": StringComparision,
    "Power is": NumericalComparision,
    "Toughness is": NumericalComparision
}

class CustomSortRule(RulePart):
    def __init__(self):
        super().__init__(SortRuleType, current_to_next_class_map)

    def should_count_card(self, card_item):
        if self.current == "Type line":
            if 'card' in card_item and 'type_line' in card_item['card']:
                # Need 3 parts, this type line, the comparision operator and the value to compare
                type_line = card_item['card']['type_line']
                comparision_operator, to_compare = self.next.get_comparision()
                return comparision_operator(type_line, to_compare)
        elif self.current == "Mana value is":
            if 'card' in card_item and 'cmc' in card_item['card']:
                # Need 3 parts, the cmc, the comparision operator and the value to compare
                cmc = card_item['card']['cmc']
                comparision_operator, to_compare = self.next.get_comparision()
                return comparision_operator(cmc, to_compare)
        elif self.current == "Oracle text":
            if 'card' in card_item and 'oracle_text' in card_item['card']:
                # Need 3 parts, the oracle text, the comparision operator and the value to compare
                oracle_text = card_item['card']['oracle_text']
                comparision_operator, to_compare = self.next.get_comparision()
                return comparision_operator(oracle_text, to_compare)
        elif self.current == "Power is":
            if 'card' in card_item and 'power' in card_item['card']:
                power = card_item['card']['power']
                comparision_operator, to_compare = self.next.get_comparision()
                return comparision_operator(power, to_compare)
        elif self.current == "Toughness is":
            if 'card' in card_item and 'toughness' in card_item['card']:
                toughness = card_item['card']['toughness']
                comparision_operator, to_compare = self.next.get_comparision()
                return comparision_operator(toughness, to_compare)