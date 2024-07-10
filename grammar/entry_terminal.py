from enum import Enum
from .rule_part import RulePart

class EntryTerminal(RulePart):
    class EntryType(Enum):
        TERMINAL = 1

    current_to_next_class_map = {
        EntryType.TERMINAL: None
    }

    enum_to_display_string_map = {
        EntryType.TERMINAL: "-"
    }

    def __init__(self):
        super().__init__(EntryTerminal.EntryType, EntryTerminal.enum_to_display_string_map, EntryTerminal.current_to_next_class_map, text_entry=True)

    def get_value(self):
        return self.text_box.get()