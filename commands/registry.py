COMMANDS = {}

def register(name):
    def wrapper(func):
        COMMANDS[name] = func
        return func
    return wrapper
