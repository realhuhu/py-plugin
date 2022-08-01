class StreamInitException(Exception):
    def __init__(self, stack):
        self.stack = stack
