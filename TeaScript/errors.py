class Error:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return f"{self.name}: {self.desc}"

# errors
ERROR_UKE = Error("UnknownCommandError", "That command is unknown")
ERROR_NEAR = Error("NotEnoughArgsError", "You did not pass enough arguments to the command you tried to execute")
