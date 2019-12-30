from Lexer import Lexer
from Parser import Parser
from Eval import Evaluator


with open("../test/function_call.ps", "r+") as f:
    lexer = Lexer(f)
    parser = Parser(lexer.tokens)
    evaluator = Evaluator(parser.AST)

    print("Tokens:")
    lexer.lex()
    print(lexer.tokens, '\n')

    print("AST:")
    parser.parse()
    print(parser.AST, "\n")

    print("Output:")
    evaluator.run(parser.AST)
