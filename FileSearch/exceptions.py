"""Custom Exceptions"""

class ExtensionError(Exception):

    def __init__(self, arg):
        self.message = arg
