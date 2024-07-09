class RulePart:
    def __init__(self, current_choices_enum, enum_to_display_string_map, current_to_next_class_map, text_entry=False):
        self.choices_enum = current_choices_enum
        self.enum_to_display_string_map = enum_to_display_string_map
        self.current_to_next_class_map = current_to_next_class_map
        self.next = None
        self.text_entry = text_entry

    def get_current_options(self):
        return [e for e in self.enum_to_display_string_map]

    def get_current_option_strings(self):
        return list(self.enum_to_display_string_map.values())

    def choose_option(self, choice):
        if choice not in self.get_current_option_strings():
            raise Exception(f'{choice} not in available current options {self.get_current_option_strings()}')
        self.current = choice
        index = list(self.enum_to_display_string_map.keys())[list(self.enum_to_display_string_map.values()).index(choice)]
        if self.current_to_next_class_map[index] is None:
            self.next = None
        else:
            self.next = self.current_to_next_class_map[index]()

    def get_next_options(self):
        if self.next is None:
            return None
        return self.next.get_current_options()

    def is_text_entry(self):
        return self.text_entry

    def should_count_card(self):
        raise "Base rule part should not be called for evaluation"