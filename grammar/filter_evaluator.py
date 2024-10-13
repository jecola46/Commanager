from .filterListener import filterListener

class FilterEvaluator(filterListener):
    def __init__(self):
        self.stack = []

    def getValue(self):
        return self.stack[0]
    
    def exitConjunctiveCondition(self, ctx):
        if ctx.getChild(2).getText() == 'and':
            second_condition = self.stack.pop()
            first_condition = self.stack.pop()
            self.stack.append(lambda card: first_condition(card) and second_condition(card))
        elif ctx.getChild(2).getText() == 'or':
            second_condition = self.stack.pop()
            first_condition = self.stack.pop()
            self.stack.append(lambda card: first_condition(card) or second_condition(card))
        else:
            print('Unknown operator: ' + ctx.getChild(1).getText())

    def exitManaCondition(self, ctx):
        mana_value = int(ctx.getChild(2).getText())
        operator = getIntComparisionFromText(ctx.getChild(1).getText())
        self.stack.append(lambda card: operator(card['cmc'], mana_value))

    def exitPowerCondition(self, ctx):
        power = int(ctx.getChild(2).getText())
        operator = getIntComparisionFromText(ctx.getChild(1).getText())
        self.stack.append(lambda card: operator(card['power'] if 'power' in card else 0, power))

    def exitToughnessCondition(self, ctx):
        toughness = int(ctx.getChild(2).getText())
        operator = getIntComparisionFromText(ctx.getChild(1).getText())
        self.stack.append(lambda card: operator(card['toughness'] if 'toughness' in card else 0, toughness))

    def exitTypeCondition(self, ctx):
        type_line = ctx.getChild(2).getText().replace('"', '')
        operator = getStringComparisionFromText(ctx.getChild(1).getText())
        self.stack.append(lambda card: operator(card['type_line'] if 'type_line' in card else '', type_line))

    def exitTextCondition(self, ctx):
        oracle_text = ctx.getChild(2).getText().replace('"', '')
        operator = getStringComparisionFromText(ctx.getChild(1).getText())
        self.stack.append(lambda card: operator(card['oracle_text'] if 'oracle_text' in card else '', oracle_text))

def getIntComparisionFromText(text):
    if text == '>':
        return lambda a, b: a > b
    elif text == '<':
        return lambda a, b: a < b
    elif text == '=':
        return lambda a, b: a == b
    else:
        print('Unknown operator: ' + text)
        
def getStringComparisionFromText(text):
    if text == 'contains':
        return lambda a, b: b.lower() in a.lower()
    elif text == 'not contains':
        return lambda a, b: b.lower() not in a.lower()
    else:
        print('Unknown operator: ' + text)