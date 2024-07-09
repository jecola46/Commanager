from enum import Enum
from .rule_part import RulePart

class EntryType(Enum):
    TERMINAL: 1

current_to_next_class_map = {
    1: None
}

enum_to_display_string_map = {
    1: "-"
}

class EntryTerminal(RulePart):
    def __init__(self):
        super().__init__(EntryType, enum_to_display_string_map, current_to_next_class_map, text_entry=True)

    def get_value(self):
        return self.text_box.get()