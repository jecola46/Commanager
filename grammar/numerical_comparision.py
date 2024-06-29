from enum import StrEnum
from .rule_part import RulePart
from .entry_terminal import EntryTerminal

class NumericalComparisionType(StrEnum):
    NOT_ENTERED = "-"
    GREATER_THAN = "Greater than"
    LESS_THAN = "Less than"
    EQUAL_TO = "Equal to"

current_to_next_class_map = {
    "-": None,
    "Greater than": EntryTerminal,
    "Less than": EntryTerminal,
    "Equal to": EntryTerminal
}

class NumericalComparision(RulePart):
    def __init__(self):
        super().__init__(NumericalComparisionType, current_to_next_class_map)

    def get_comparision(self):
        def compare(value_one, value_two):
            if self.current == "Greater than":
                return int(value_one) > int(value_two)
            elif self.current == "Less than":
                return int(value_one) < int(value_two)
            elif self.current == "Equal to":
                return int(value_one) == int(value_two)

        return compare, self.next.get_value()