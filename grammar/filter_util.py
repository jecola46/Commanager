import sys
from antlr4 import *
from .filterLexer import filterLexer
from .filterParser import filterParser
from .filter_evaluator import FilterEvaluator

def create_filter_from_string(filter_string):
    input_stream = InputStream(filter_string)
    lexer = filterLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = filterParser(stream)
    filter_evaluator = FilterEvaluator()
    parser.addParseListener(filter_evaluator)
    tree = parser.filter_()
    return filter_evaluator.getValue()