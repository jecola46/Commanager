import tkinter as tk

class CustomSortWindow(tk.Toplevel):
    def __init__(self, parent, rule_var):
        super().__init__(parent)
        self.title("Add Custom Sort")
        self.rule_var = rule_var

        # Define card traits and operators
        self.card_traits = ["mana value", "power", "toughness", "text", "type"]
        self.numerical_operators = ["equal to", "greater than", "less than"]
        self.string_operators = ["contains", "not contains"]

        # Define functions to help serialize rules
        self.trait_to_printable_rule = {
            "mana value": "mana value",
            "power": "power",
            "toughness": "toughness",
            "text": "text",
            "type": "type",
            "equal to": "=",
            "greater than": ">",
            "less than": "<",
            "contains": "contains",
            "not contains": "not contains"
        }

        # Initialize variables
        self.container = tk.Frame(self) 
        self.rule_frame = tk.Frame(self.container)
        self.buttons_frame = tk.Frame(self.container)
        self.trait_var = tk.StringVar(self)
        self.operator_var = tk.StringVar(self)
        self.value_entry = tk.Entry(self.rule_frame)

        # Create UI elements
        self.create_ui()

    def create_ui(self):
        # Function to update operators based on selected trait
        def update_operators(*args):
            selected_trait = self.trait_var.get()
            if selected_trait in ["mana value", "power", "toughness"]:
                operator_menu['menu'].delete(0, 'end')
                for operator in self.numerical_operators:
                    operator_menu['menu'].add_command(label=operator, command=tk._setit(self.operator_var, operator))
                self.operator_var.set(self.numerical_operators[0])
            else:
                operator_menu['menu'].delete(0, 'end')
                for operator in self.string_operators:
                    operator_menu['menu'].add_command(label=operator, command=tk._setit(self.operator_var, operator))
                self.operator_var.set(self.string_operators[0])

        # Containers
        self.container.grid(pady=25, padx=30)
        self.rule_frame.grid()
        self.buttons_frame.grid(pady=(7, 0))

        # Card trait dropdown
        self.trait_var.set(self.card_traits[0])
        self.trait_var.trace("w", update_operators)
        trait_menu = tk.OptionMenu(self.rule_frame, self.trait_var, *self.card_traits)
        trait_menu.pack(side = tk.LEFT)

        # Comparison operator dropdown
        self.operator_var.set(self.numerical_operators[0])
        operator_menu = tk.OptionMenu(self.rule_frame, self.operator_var, *self.numerical_operators)
        operator_menu.pack(side = tk.LEFT)

        # Value entry
        self.value_entry.pack(side = tk.LEFT)

        # Save and cancel buttons
        save_button = tk.Button(self.buttons_frame, text="Save", command=self.save_rule)
        save_button.pack(side = tk.LEFT)
        cancel_button = tk.Button(self.buttons_frame, text="Cancel", command=self.destroy)
        cancel_button.pack(side = tk.RIGHT)

    def save_rule(self):
        trait = self.trait_var.get()
        operator = self.operator_var.get()
        value = self.value_entry.get()
        selected_trait = self.trait_var.get()
        if selected_trait not in ["mana value", "power", "toughness"]:
            value = f'"{value}"'
        rule = f"{self.trait_to_printable_rule[trait]} {self.trait_to_printable_rule[operator]} {value}"
        print(f"Saved rule: {rule}")
        self.rule_var.set(rule)
        self.destroy()