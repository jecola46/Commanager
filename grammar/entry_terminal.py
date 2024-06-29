from enum import StrEnum
from .rule_part import RulePart

class EntryType(StrEnum):
    TERMINAL: "-"

current_to_next_class_map = {
    "-": None
}

class EntryTerminal(RulePart):
    def __init__(self):
        super().__init__(EntryType, current_to_next_class_map, text_entry=True)

    def get_value(self):
        return self.text_box.get()