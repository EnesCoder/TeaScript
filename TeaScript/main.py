# pyright: reportMissingImports=false

import os
from interpret import interpret

INPUT_SHUSH = ">>>"

if __name__ == "__main__":
    while True:
        inp: str = input(f"{os.getcwd()} {INPUT_SHUSH} ")
        err = interpret(inp)
        if err:
            print(err)
            break
