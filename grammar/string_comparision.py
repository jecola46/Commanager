from enum import StrEnum
from .rule_part import RulePart
from .entry_terminal import EntryTerminal

class StringComparisionType(StrEnum):
    NOT_ENTERED = "-"
    CONTAINS = "Contains"
    NOT_CONTAINS = "Does not contain"

current_to_next_class_map = {
    "-": None,
    "Contains": EntryTerminal,
    "Does not contain": EntryTerminal
}

class StringComparision(RulePart):
    def __init__(self):
        super().__init__(StringComparisionType, current_to_next_class_map)

    def get_comparision(self):
        def compare(value_one, value_two):
            if self.current == "Contains":
                return value_two.lower() in value_one.lower()
            elif self.current == "Does not contain":
                return value_two.lower() not in value_one.lower()
        return compare, self.next.get_value()