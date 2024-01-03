# pyright: reportMissingImports=false

import actions
from errors import Error, ERROR_UKE, ERROR_NEAR

class Command:
    def __init__(self, name: str, arg_cnt: int, action):
        self.name = name
        self.arg_cnt = arg_cnt
        self.action = action

    def __repr__(self):
        return f"command {self.name}, needs {self.arg_cnt} arguments and what it does is {self.action}"

    def execute(self, args):
        self.action(args)

AVAIL_COMS = [Command("echo", 1, actions.echo)]

def find_com_by_name(name: str) -> tuple[Error | None, Command | None]:
    for com in AVAIL_COMS:
        if com.name == name:
            return (None, com)
    return (ERROR_UKE, None)

def exec_com(name: str, com_args) -> Error | None:
    (err, com) = find_com_by_name(name)
    if err:
        return err
    elif com:
        if len(com_args) != com.arg_cnt:
            return ERROR_NEAR
        com.execute(com_args)
    return None
