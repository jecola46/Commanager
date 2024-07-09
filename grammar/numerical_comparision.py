from enum import Enum
from .rule_part import RulePart
from .entry_terminal import EntryTerminal

class NumericalComparisionType(Enum):
    NOT_ENTERED = 1
    GREATER_THAN = 2
    LESS_THAN = 3
    EQUAL_TO = 4

enum_to_display_string_map = {
    1: "-",
    2: "Greater than",
    3: "Less than",
    4: "Equal to"
}

current_to_next_class_map = {
    1: None,
    2: EntryTerminal,
    3: EntryTerminal,
    4: EntryTerminal
}

class NumericalComparision(RulePart):
    def __init__(self):
        super().__init__(NumericalComparisionType, enum_to_display_string_map, current_to_next_class_map)

    def get_comparision(self):
        def compare(value_one, value_two):
            try:
                if self.current == "Greater than":
                    return int(value_one) > int(value_two)
                elif self.current == "Less than":
                    return int(value_one) < int(value_two)
                elif self.current == "Equal to":
                    return int(value_one) == int(value_two)
            except ValueError:
                return False

        return compare, self.next.get_value()