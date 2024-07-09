from enum import Enum
from .rule_part import RulePart
from .entry_terminal import EntryTerminal

class StringComparisionType(Enum):
    NOT_ENTERED = 1
    CONTAINS = 2
    NOT_CONTAINS = 3

enum_to_display_string_map = {
    1: "-",
    2: "Contains",
    3: "Does not contain"
}

current_to_next_class_map = {
    1: None,
    2: EntryTerminal,
    3: EntryTerminal
}

class StringComparision(RulePart):
    def __init__(self):
        super().__init__(StringComparisionType, enum_to_display_string_map, current_to_next_class_map)

    def get_comparision(self):
        def compare(value_one, value_two):
            if self.current == "Contains":
                return value_two.lower() in value_one.lower()
            elif self.current == "Does not contain":
                return value_two.lower() not in value_one.lower()
        return compare, self.next.get_value()