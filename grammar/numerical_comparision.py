from enum import Enum
from .rule_part import RulePart
from .entry_terminal import EntryTerminal

class NumericalComparision(RulePart):
    class NumericalComparisionType(Enum):
        NOT_ENTERED = 1
        GREATER_THAN = 2
        LESS_THAN = 3
        EQUAL_TO = 4

    enum_to_display_string_map = {
        NumericalComparisionType.NOT_ENTERED: "-",
        NumericalComparisionType.GREATER_THAN: "Greater than",
        NumericalComparisionType.LESS_THAN: "Less than",
        NumericalComparisionType.EQUAL_TO: "Equal to"
    }

    current_to_next_class_map = {
        NumericalComparisionType.NOT_ENTERED: None,
        NumericalComparisionType.GREATER_THAN: EntryTerminal,
        NumericalComparisionType.LESS_THAN: EntryTerminal,
        NumericalComparisionType.EQUAL_TO: EntryTerminal
    }

    def __init__(self):
        super().__init__(self.NumericalComparisionType, NumericalComparision.enum_to_display_string_map, NumericalComparision.current_to_next_class_map)

    def get_comparision(self):
        def compare(value_one, value_two):
            try:
                if self.current == self.NumericalComparisionType.GREATER_THAN:
                    return int(value_one) > int(value_two)
                elif self.current == self.NumericalComparisionType.LESS_THAN:
                    return int(value_one) < int(value_two)
                elif self.current == self.NumericalComparisionType.EQUAL_TO:
                    return int(value_one) == int(value_two)
            except ValueError:
                return False

        return compare, self.next.get_value()