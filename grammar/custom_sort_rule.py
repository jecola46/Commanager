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
            if 'type_line' in card_item:
                # Need 3 parts, this type line, the comparision operator and the value to compare
                type_line = card_item['type_line']
                comparision_operator, to_compare = self.next.get_comparision()
                return comparision_operator(type_line, to_compare)
        elif self.current == CustomSortRule.SortRuleType.MANA_VALUE:
            if 'cmc' in card_item:
                # Need 3 parts, the cmc, the comparision operator and the value to compare
                cmc = card_item['cmc']
                comparision_operator, to_compare = self.next.get_comparision()
                return comparision_operator(cmc, to_compare)
        elif self.current == CustomSortRule.SortRuleType.ORACLE_TEXT:
            if 'oracle_text' in card_item:
                # Need 3 parts, the oracle text, the comparision operator and the value to compare
                oracle_text = card_item['oracle_text']
                comparision_operator, to_compare = self.next.get_comparision()
                return comparision_operator(oracle_text, to_compare)
        elif self.current == CustomSortRule.SortRuleType.POWER:
            if 'power' in card_item:
                power = card_item['power']
                comparision_operator, to_compare = self.next.get_comparision()
                return comparision_operator(power, to_compare)
        elif self.current == CustomSortRule.SortRuleType.TOUGHNESS:
            if 'toughness' in card_item:
                toughness = card_item['toughness']
                comparision_operator, to_compare = self.next.get_comparision()
                return comparision_operator(toughness, to_compare)