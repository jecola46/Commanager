# Generated from grammar/filter.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .filterParser import filterParser
else:
    from filterParser import filterParser

# This class defines a complete listener for a parse tree produced by filterParser.
class filterListener(ParseTreeListener):

    # Enter a parse tree produced by filterParser#filter.
    def enterFilter(self, ctx:filterParser.FilterContext):
        pass

    # Exit a parse tree produced by filterParser#filter.
    def exitFilter(self, ctx:filterParser.FilterContext):
        pass


    # Enter a parse tree produced by filterParser#condition.
    def enterCondition(self, ctx:filterParser.ConditionContext):
        pass

    # Exit a parse tree produced by filterParser#condition.
    def exitCondition(self, ctx:filterParser.ConditionContext):
        pass


    # Enter a parse tree produced by filterParser#conjunctiveCondition.
    def enterConjunctiveCondition(self, ctx:filterParser.ConjunctiveConditionContext):
        pass

    # Exit a parse tree produced by filterParser#conjunctiveCondition.
    def exitConjunctiveCondition(self, ctx:filterParser.ConjunctiveConditionContext):
        pass


    # Enter a parse tree produced by filterParser#manaCondition.
    def enterManaCondition(self, ctx:filterParser.ManaConditionContext):
        pass

    # Exit a parse tree produced by filterParser#manaCondition.
    def exitManaCondition(self, ctx:filterParser.ManaConditionContext):
        pass


    # Enter a parse tree produced by filterParser#powerCondition.
    def enterPowerCondition(self, ctx:filterParser.PowerConditionContext):
        pass

    # Exit a parse tree produced by filterParser#powerCondition.
    def exitPowerCondition(self, ctx:filterParser.PowerConditionContext):
        pass


    # Enter a parse tree produced by filterParser#toughnessCondition.
    def enterToughnessCondition(self, ctx:filterParser.ToughnessConditionContext):
        pass

    # Exit a parse tree produced by filterParser#toughnessCondition.
    def exitToughnessCondition(self, ctx:filterParser.ToughnessConditionContext):
        pass


    # Enter a parse tree produced by filterParser#textCondition.
    def enterTextCondition(self, ctx:filterParser.TextConditionContext):
        pass

    # Exit a parse tree produced by filterParser#textCondition.
    def exitTextCondition(self, ctx:filterParser.TextConditionContext):
        pass


    # Enter a parse tree produced by filterParser#typeCondition.
    def enterTypeCondition(self, ctx:filterParser.TypeConditionContext):
        pass

    # Exit a parse tree produced by filterParser#typeCondition.
    def exitTypeCondition(self, ctx:filterParser.TypeConditionContext):
        pass


    # Enter a parse tree produced by filterParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:filterParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by filterParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:filterParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by filterParser#textOperator.
    def enterTextOperator(self, ctx:filterParser.TextOperatorContext):
        pass

    # Exit a parse tree produced by filterParser#textOperator.
    def exitTextOperator(self, ctx:filterParser.TextOperatorContext):
        pass


    # Enter a parse tree produced by filterParser#logicalOperator.
    def enterLogicalOperator(self, ctx:filterParser.LogicalOperatorContext):
        pass

    # Exit a parse tree produced by filterParser#logicalOperator.
    def exitLogicalOperator(self, ctx:filterParser.LogicalOperatorContext):
        pass



del filterParser