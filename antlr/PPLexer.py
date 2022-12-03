# Generated from ./antlr/PP.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\30")
        buf.write("p\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write("\2\2\30\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27")
        buf.write("-\30\3\2\3\3\2\63;\2o\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\3/\3\2\2\2\5\66\3\2\2\2\79\3\2")
        buf.write("\2\2\t?\3\2\2\2\13C\3\2\2\2\rE\3\2\2\2\17G\3\2\2\2\21")
        buf.write("J\3\2\2\2\23M\3\2\2\2\25O\3\2\2\2\27Q\3\2\2\2\31S\3\2")
        buf.write("\2\2\33W\3\2\2\2\35Z\3\2\2\2\37\\\3\2\2\2!^\3\2\2\2#`")
        buf.write("\3\2\2\2%b\3\2\2\2\'h\3\2\2\2)j\3\2\2\2+l\3\2\2\2-n\3")
        buf.write("\2\2\2/\60\7r\2\2\60\61\7t\2\2\61\62\7k\2\2\62\63\7p\2")
        buf.write("\2\63\64\7v\2\2\64\65\7*\2\2\65\4\3\2\2\2\66\67\7+\2\2")
        buf.write("\678\7=\2\28\6\3\2\2\29:\7k\2\2:;\7p\2\2;<\7r\2\2<=\7")
        buf.write("w\2\2=>\7v\2\2>\b\3\2\2\2?@\7K\2\2@A\7H\2\2AB\7*\2\2B")
        buf.write("\n\3\2\2\2CD\7+\2\2D\f\3\2\2\2EF\7=\2\2F\16\3\2\2\2GH")
        buf.write("\7?\2\2HI\7?\2\2I\20\3\2\2\2JK\7#\2\2KL\7?\2\2L\22\3\2")
        buf.write("\2\2MN\7@\2\2N\24\3\2\2\2OP\7>\2\2P\26\3\2\2\2QR\7*\2")
        buf.write("\2R\30\3\2\2\2ST\7C\2\2TU\7P\2\2UV\7F\2\2V\32\3\2\2\2")
        buf.write("WX\7Q\2\2XY\7T\2\2Y\34\3\2\2\2Z[\7-\2\2[\36\3\2\2\2\\")
        buf.write("]\7/\2\2] \3\2\2\2^_\7\61\2\2_\"\3\2\2\2`a\7,\2\2a$\3")
        buf.write("\2\2\2bc\7N\2\2cd\7Q\2\2de\7Q\2\2ef\7R\2\2fg\7*\2\2g&")
        buf.write("\3\2\2\2hi\7?\2\2i(\3\2\2\2jk\7Z\2\2k*\3\2\2\2lm\t\2\2")
        buf.write("\2m,\3\2\2\2no\7\62\2\2o.\3\2\2\2\3\2\2")
        return buf.getvalue()


class PPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    NONZERODIGIT = 21
    ZERO = 22

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'print('", "');'", "'input'", "'IF('", "')'", "';'", "'=='", 
            "'!='", "'>'", "'<'", "'('", "'AND'", "'OR'", "'+'", "'-'", 
            "'/'", "'*'", "'LOOP('", "'='", "'X'", "'0'" ]

    symbolicNames = [ "<INVALID>",
            "NONZERODIGIT", "ZERO" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "NONZERODIGIT", "ZERO" ]

    grammarFileName = "PP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

