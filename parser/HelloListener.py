# Generated from Hello.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete listener for a parse tree produced by HelloParser.
class HelloListener(ParseTreeListener):

    # Enter a parse tree produced by HelloParser#r.
    def enterR(self, ctx:HelloParser.RContext):
        pass

    # Exit a parse tree produced by HelloParser#r.
    def exitR(self, ctx:HelloParser.RContext):
        pass


    # Enter a parse tree produced by HelloParser#name.
    def enterName(self, ctx:HelloParser.NameContext):
        pass

    # Exit a parse tree produced by HelloParser#name.
    def exitName(self, ctx:HelloParser.NameContext):
        pass



del HelloParser