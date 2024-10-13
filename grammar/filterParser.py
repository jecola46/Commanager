# Generated from grammar/filter.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,66,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,
        4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,
        8,1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,3,
        1,0,8,10,1,0,11,12,1,0,13,14,59,0,22,1,0,0,0,2,31,1,0,0,0,4,33,1,
        0,0,0,6,39,1,0,0,0,8,43,1,0,0,0,10,47,1,0,0,0,12,51,1,0,0,0,14,55,
        1,0,0,0,16,59,1,0,0,0,18,61,1,0,0,0,20,63,1,0,0,0,22,23,3,2,1,0,
        23,24,5,0,0,1,24,1,1,0,0,0,25,32,3,6,3,0,26,32,3,12,6,0,27,32,3,
        10,5,0,28,32,3,8,4,0,29,32,3,14,7,0,30,32,3,4,2,0,31,25,1,0,0,0,
        31,26,1,0,0,0,31,27,1,0,0,0,31,28,1,0,0,0,31,29,1,0,0,0,31,30,1,
        0,0,0,32,3,1,0,0,0,33,34,5,1,0,0,34,35,3,2,1,0,35,36,3,20,10,0,36,
        37,3,2,1,0,37,38,5,2,0,0,38,5,1,0,0,0,39,40,5,3,0,0,40,41,3,16,8,
        0,41,42,5,15,0,0,42,7,1,0,0,0,43,44,5,4,0,0,44,45,3,16,8,0,45,46,
        5,15,0,0,46,9,1,0,0,0,47,48,5,5,0,0,48,49,3,16,8,0,49,50,5,15,0,
        0,50,11,1,0,0,0,51,52,5,6,0,0,52,53,3,18,9,0,53,54,5,16,0,0,54,13,
        1,0,0,0,55,56,5,7,0,0,56,57,3,18,9,0,57,58,5,16,0,0,58,15,1,0,0,
        0,59,60,7,0,0,0,60,17,1,0,0,0,61,62,7,1,0,0,62,19,1,0,0,0,63,64,
        7,2,0,0,64,21,1,0,0,0,1,31
    ]

class filterParser ( Parser ):

    grammarFileName = "filter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'mana value'", "'power'", 
                     "'toughness'", "'text'", "'type'", "'='", "'<'", "'>'", 
                     "'contains'", "'not contains'", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "AND", "OR", "INT", "STRING", "WS" ]

    RULE_filter = 0
    RULE_condition = 1
    RULE_conjunctiveCondition = 2
    RULE_manaCondition = 3
    RULE_powerCondition = 4
    RULE_toughnessCondition = 5
    RULE_textCondition = 6
    RULE_typeCondition = 7
    RULE_comparisonOperator = 8
    RULE_textOperator = 9
    RULE_logicalOperator = 10

    ruleNames =  [ "filter", "condition", "conjunctiveCondition", "manaCondition", 
                   "powerCondition", "toughnessCondition", "textCondition", 
                   "typeCondition", "comparisonOperator", "textOperator", 
                   "logicalOperator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    AND=13
    OR=14
    INT=15
    STRING=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FilterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(filterParser.ConditionContext,0)


        def EOF(self):
            return self.getToken(filterParser.EOF, 0)

        def getRuleIndex(self):
            return filterParser.RULE_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilter" ):
                listener.enterFilter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilter" ):
                listener.exitFilter(self)




    def filter_(self):

        localctx = filterParser.FilterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.condition()
            self.state = 23
            self.match(filterParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def manaCondition(self):
            return self.getTypedRuleContext(filterParser.ManaConditionContext,0)


        def textCondition(self):
            return self.getTypedRuleContext(filterParser.TextConditionContext,0)


        def toughnessCondition(self):
            return self.getTypedRuleContext(filterParser.ToughnessConditionContext,0)


        def powerCondition(self):
            return self.getTypedRuleContext(filterParser.PowerConditionContext,0)


        def typeCondition(self):
            return self.getTypedRuleContext(filterParser.TypeConditionContext,0)


        def conjunctiveCondition(self):
            return self.getTypedRuleContext(filterParser.ConjunctiveConditionContext,0)


        def getRuleIndex(self):
            return filterParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = filterParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_condition)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.manaCondition()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.textCondition()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.toughnessCondition()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.powerCondition()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 29
                self.typeCondition()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 6)
                self.state = 30
                self.conjunctiveCondition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConjunctiveConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(filterParser.ConditionContext)
            else:
                return self.getTypedRuleContext(filterParser.ConditionContext,i)


        def logicalOperator(self):
            return self.getTypedRuleContext(filterParser.LogicalOperatorContext,0)


        def getRuleIndex(self):
            return filterParser.RULE_conjunctiveCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunctiveCondition" ):
                listener.enterConjunctiveCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunctiveCondition" ):
                listener.exitConjunctiveCondition(self)




    def conjunctiveCondition(self):

        localctx = filterParser.ConjunctiveConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_conjunctiveCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(filterParser.T__0)
            self.state = 34
            self.condition()
            self.state = 35
            self.logicalOperator()
            self.state = 36
            self.condition()
            self.state = 37
            self.match(filterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManaConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparisonOperator(self):
            return self.getTypedRuleContext(filterParser.ComparisonOperatorContext,0)


        def INT(self):
            return self.getToken(filterParser.INT, 0)

        def getRuleIndex(self):
            return filterParser.RULE_manaCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterManaCondition" ):
                listener.enterManaCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitManaCondition" ):
                listener.exitManaCondition(self)




    def manaCondition(self):

        localctx = filterParser.ManaConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_manaCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(filterParser.T__2)
            self.state = 40
            self.comparisonOperator()
            self.state = 41
            self.match(filterParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowerConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparisonOperator(self):
            return self.getTypedRuleContext(filterParser.ComparisonOperatorContext,0)


        def INT(self):
            return self.getToken(filterParser.INT, 0)

        def getRuleIndex(self):
            return filterParser.RULE_powerCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowerCondition" ):
                listener.enterPowerCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowerCondition" ):
                listener.exitPowerCondition(self)




    def powerCondition(self):

        localctx = filterParser.PowerConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_powerCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(filterParser.T__3)
            self.state = 44
            self.comparisonOperator()
            self.state = 45
            self.match(filterParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToughnessConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparisonOperator(self):
            return self.getTypedRuleContext(filterParser.ComparisonOperatorContext,0)


        def INT(self):
            return self.getToken(filterParser.INT, 0)

        def getRuleIndex(self):
            return filterParser.RULE_toughnessCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToughnessCondition" ):
                listener.enterToughnessCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToughnessCondition" ):
                listener.exitToughnessCondition(self)




    def toughnessCondition(self):

        localctx = filterParser.ToughnessConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_toughnessCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(filterParser.T__4)
            self.state = 48
            self.comparisonOperator()
            self.state = 49
            self.match(filterParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def textOperator(self):
            return self.getTypedRuleContext(filterParser.TextOperatorContext,0)


        def STRING(self):
            return self.getToken(filterParser.STRING, 0)

        def getRuleIndex(self):
            return filterParser.RULE_textCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTextCondition" ):
                listener.enterTextCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTextCondition" ):
                listener.exitTextCondition(self)




    def textCondition(self):

        localctx = filterParser.TextConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_textCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(filterParser.T__5)
            self.state = 52
            self.textOperator()
            self.state = 53
            self.match(filterParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def textOperator(self):
            return self.getTypedRuleContext(filterParser.TextOperatorContext,0)


        def STRING(self):
            return self.getToken(filterParser.STRING, 0)

        def getRuleIndex(self):
            return filterParser.RULE_typeCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeCondition" ):
                listener.enterTypeCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeCondition" ):
                listener.exitTypeCondition(self)




    def typeCondition(self):

        localctx = filterParser.TypeConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typeCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(filterParser.T__6)
            self.state = 56
            self.textOperator()
            self.state = 57
            self.match(filterParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return filterParser.RULE_comparisonOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperator" ):
                listener.enterComparisonOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperator" ):
                listener.exitComparisonOperator(self)




    def comparisonOperator(self):

        localctx = filterParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return filterParser.RULE_textOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTextOperator" ):
                listener.enterTextOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTextOperator" ):
                listener.exitTextOperator(self)




    def textOperator(self):

        localctx = filterParser.TextOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_textOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(filterParser.AND, 0)

        def OR(self):
            return self.getToken(filterParser.OR, 0)

        def getRuleIndex(self):
            return filterParser.RULE_logicalOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOperator" ):
                listener.enterLogicalOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOperator" ):
                listener.exitLogicalOperator(self)




    def logicalOperator(self):

        localctx = filterParser.LogicalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_logicalOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





