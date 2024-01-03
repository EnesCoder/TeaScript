# pyright: reportMissingImports=false

from commands import exec_com
from errors import Error

def tokenize(code: str):
    code = code.strip()

    cur_tok: str = ""
    tokens = []
    in_quotes: bool = False

    for c in code:
        if c not in " \n" or in_quotes:
            if c in "\"'":
                in_quotes = not in_quotes
            else:
                cur_tok += c
        else:
            tokens.append(cur_tok)
            cur_tok = ""

    tokens.append(cur_tok)
    return tokens

def interpret(code: str) -> Error | None:
    # tokenization
    tokens = tokenize(code)

    # execute the command
    com = tokens[0]
    com_args = tokens[1:]

    err = exec_com(com, com_args)
    if err:
        return err
    return None
