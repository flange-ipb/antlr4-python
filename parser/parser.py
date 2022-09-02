from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

from parser.HelloLexer import HelloLexer
from parser.HelloListener import HelloListener
from parser.HelloParser import HelloParser


def parse_r(s):
    parser = _prepare_parser(s)

    # invoke the parser on rule "r"
    tree = parser.r()

    walker = ParseTreeWalker()
    listener = HelloListenerImpl()
    walker.walk(listener, tree)

    return listener.names


def parse_name(s):
    parser = _prepare_parser(s)

    # invoke the parser on rule "name"
    tree = parser.name()

    return list(map(lambda id: id.getText(), tree.ID()))


def _prepare_parser(s):
    stream = InputStream(s)
    lexer = HelloLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = HelloParser(token_stream)
    # register our own error listeners
    lexer.removeErrorListeners()
    lexer.addErrorListener(LexerErrorListener())
    parser.removeErrorListeners()
    parser.addErrorListener(ParserErrorListener())
    return parser


class HelloListenerImpl(HelloListener):
    def __init__(self):
        self.names = []

    def enterName(self, ctx: HelloParser.NameContext):
        full_name = " ".join(list(map(lambda id: id.getText(), ctx.ID())))
        self.names.append(full_name)


class RaisingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        error_str = "line " + str(line) + ":" + str(column) + " " + msg + "\n"
        error_str += self._underline_error(recognizer, offending_symbol, line, column)
        raise ParseCancellationException(error_str)

    def _underline_error(self, recognizer, offending_symbol, line, column):
        pass


# The algorithm of underline_error was adopted from Terence Parr's book "The Definitive ANTLR 4 Reference", page 156.
class LexerErrorListener(RaisingErrorListener):
    def _underline_error(self, recognizer, offending_symbol, line, column):
        lexer_input = str(recognizer.inputStream)
        error_line = lexer_input.split("\n")[line - 1]

        output = error_line + "\n"
        for _ in range(0, column):
            output += " "
        output += "^"
        return output


class ParserErrorListener(RaisingErrorListener):
    def _underline_error(self, recognizer, offending_symbol, line, column):
        tokens = recognizer.getInputStream()
        parser_input = str(tokens.tokenSource.inputStream)
        error_line = parser_input.split("\n")[line - 1]

        output = error_line + "\n"
        for _ in range(0, column):
            output += " "

        start = offending_symbol.start
        stop = offending_symbol.stop
        if 0 <= start <= stop:
            for _ in range(start, stop + 1):
                output += "^"
        return output
