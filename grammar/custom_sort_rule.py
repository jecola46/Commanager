from enum import Enum
from .rule_part import RulePart
from .string_comparision import StringComparision
from .numerical_comparision import NumericalComparision

class CustomSortRule(RulePart):
    class SortRuleType(Enum):
        NOT_ENTERED = 1
        TYPE_LINE = 2
        MANA_VALUE = 3
        ORACLE_TEXT = 4
        POWER = 5
        TOUGHNESS = 6

    enum_to_display_string_map = {
        SortRuleType.NOT_ENTERED: "-",
        SortRuleType.TYPE_LINE: "Type line",
        SortRuleType.MANA_VALUE: "Mana value is",
        SortRuleType.ORACLE_TEXT: "Oracle text",
        SortRuleType.POWER: "Power is",
        SortRuleType.TOUGHNESS: "Toughness is"
    }

    current_to_next_class_map = {
        SortRuleType.NOT_ENTERED: None,
        SortRuleType.TYPE_LINE: StringComparision,
        SortRuleType.MANA_VALUE: NumericalComparision,
        SortRuleType.ORACLE_TEXT: StringComparision,
        SortRuleType.POWER: NumericalComparision,
        SortRuleType.TOUGHNESS: NumericalComparision
    }

    def __init__(self):
        super().__init__(CustomSortRule.SortRuleType, CustomSortRule.enum_to_display_string_map, CustomSortRule.current_to_next_class_map)

    def should_count_card(self, card_item):
        if self.current == CustomSortRule.SortRuleType.TYPE_LINE:
            if 'card' in card_item and 'type_line' in card_item['card']:
                # Need 3 parts, this type line, the comparision operator and the value to compare
                type_line = card_item['card']['type_line']
                comparision_operator, to_compare = self.next.get_comparision()
                return comparision_operator(type_line, to_compare)
        elif self.current == CustomSortRule.SortRuleType.MANA_VALUE:
            if 'card' in card_item and 'cmc' in card_item['card']:
                # Need 3 parts, the cmc, the comparision operator and the value to compare
                cmc = card_item['card']['cmc']
                comparision_operator, to_compare = self.next.get_comparision()
                return comparision_operator(cmc, to_compare)
        elif self.current == CustomSortRule.SortRuleType.ORACLE_TEXT:
            if 'card' in card_item and 'oracle_text' in card_item['card']:
                # Need 3 parts, the oracle text, the comparision operator and the value to compare
                oracle_text = card_item['card']['oracle_text']
                comparision_operator, to_compare = self.next.get_comparision()
                return comparision_operator(oracle_text, to_compare)
        elif self.current == CustomSortRule.SortRuleType.POWER:
            if 'card' in card_item and 'power' in card_item['card']:
                power = card_item['card']['power']
                comparision_operator, to_compare = self.next.get_comparision()
                return comparision_operator(power, to_compare)
        elif self.current == CustomSortRule.SortRuleType.TOUGHNESS:
            if 'card' in card_item and 'toughness' in card_item['card']:
                toughness = card_item['card']['toughness']
                comparision_operator, to_compare = self.next.get_comparision()
                return comparision_operator(toughness, to_compare)