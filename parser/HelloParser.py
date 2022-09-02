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
        4,1,4,23,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,5,0,9,8,0,10,0,12,0,12,
        9,0,1,1,1,1,5,1,16,8,1,10,1,12,1,19,9,1,1,1,1,1,1,1,0,0,2,0,2,0,
        0,22,0,4,1,0,0,0,2,13,1,0,0,0,4,5,5,1,0,0,5,10,3,2,1,0,6,7,5,2,0,
        0,7,9,3,2,1,0,8,6,1,0,0,0,9,12,1,0,0,0,10,8,1,0,0,0,10,11,1,0,0,
        0,11,1,1,0,0,0,12,10,1,0,0,0,13,17,5,3,0,0,14,16,5,3,0,0,15,14,1,
        0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,20,1,0,0,0,19,
        17,1,0,0,0,20,21,5,3,0,0,21,3,1,0,0,0,2,10,17
    ]

class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'hello'", "'and'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ID", "WS" ]

    RULE_r = 0
    RULE_name = 1

    ruleNames =  [ "r", "name" ]

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

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.NameContext)
            else:
                return self.getTypedRuleContext(HelloParser.NameContext,i)


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
            self.state = 4
            self.match(HelloParser.T__0)
            self.state = 5
            self.name()
            self.state = 10
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HelloParser.T__1:
                self.state = 6
                self.match(HelloParser.T__1)
                self.state = 7
                self.name()
                self.state = 12
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
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
            return HelloParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = HelloParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(HelloParser.ID)
            self.state = 17
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 14
                    self.match(HelloParser.ID) 
                self.state = 19
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 20
            self.match(HelloParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





