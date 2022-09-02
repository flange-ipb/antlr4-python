# Generated from Hello.g4 by ANTLR 4.10.1
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
        4,1,4,12,2,0,7,0,1,0,1,0,1,0,1,0,5,0,7,8,0,10,0,12,0,10,9,0,1,0,
        0,0,1,0,0,0,11,0,2,1,0,0,0,2,3,5,1,0,0,3,8,5,3,0,0,4,5,5,2,0,0,5,
        7,5,3,0,0,6,4,1,0,0,0,7,10,1,0,0,0,8,6,1,0,0,0,8,9,1,0,0,0,9,1,1,
        0,0,0,10,8,1,0,0,0,1,8
    ]

class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'hello'", "'and'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ID", "WS" ]

    RULE_r = 0

    ruleNames =  [ "r" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ID=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.ID)
            else:
                return self.getToken(HelloParser.ID, i)

        def getRuleIndex(self):
            return HelloParser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR" ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR" ):
                listener.exitR(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR" ):
                return visitor.visitR(self)
            else:
                return visitor.visitChildren(self)




    def r(self):

        localctx = HelloParser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(HelloParser.T__0)
            self.state = 3
            self.match(HelloParser.ID)
            self.state = 8
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HelloParser.T__1:
                self.state = 4
                self.match(HelloParser.T__1)
                self.state = 5
                self.match(HelloParser.ID)
                self.state = 10
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





