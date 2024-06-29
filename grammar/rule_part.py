class RulePart:
    def __init__(self, current_choices_enum, current_to_next_class_map, text_entry=False):
        self.choices_enum = current_choices_enum
        self.current_to_next_class_map = current_to_next_class_map
        self.next = None
        self.text_entry = text_entry

    def get_current_options(self):
        return [e for e in self.choices_enum]

    def get_current_option_strings(self):
        return [e.value for e in self.choices_enum]

    def choose_option(self, choice):
        if choice not in self.get_current_option_strings():
            raise f'{current_option} not in available current options {get_current_option_strings()}'
        self.current = choice
        if self.current_to_next_class_map[self.current] is None:
            self.next = None
        else:
            self.next = self.current_to_next_class_map[self.current]()

    def get_next_options(self):
        if self.next is None:
            return None
        return self.next.get_current_options()

    def is_text_entry(self):
        return self.text_entry

    def should_count_card(self):
        raise "Base rule part should not be called for evaluation"