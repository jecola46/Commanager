from enum import Enum
from .rule_part import RulePart
from .entry_terminal import EntryTerminal

class StringComparision(RulePart):
    class StringComparisionType(Enum):
        NOT_ENTERED = 1
        CONTAINS = 2
        NOT_CONTAINS = 3

    enum_to_display_string_map = {
        StringComparisionType.NOT_ENTERED: "-",
        StringComparisionType.CONTAINS: "Contains",
        StringComparisionType.NOT_CONTAINS: "Does not contain"
    }

    current_to_next_class_map = {
        StringComparisionType.NOT_ENTERED: None,
        StringComparisionType.CONTAINS: EntryTerminal,
        StringComparisionType.NOT_CONTAINS: EntryTerminal
    }

    def __init__(self):
        super().__init__(StringComparision.StringComparisionType, StringComparision.enum_to_display_string_map, StringComparision.current_to_next_class_map)

    def get_comparision(self):
        def compare(value_one, value_two):
            if self.current == StringComparision.StringComparisionType.CONTAINS:
                return value_two.lower() in value_one.lower()
            elif self.current == StringComparision.StringComparisionType.NOT_CONTAINS:
                return value_two.lower() not in value_one.lower()
        return compare, self.next.get_value()