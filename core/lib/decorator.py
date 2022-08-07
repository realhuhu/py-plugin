class Handler:
    @staticmethod
    def FrameToStream(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.__type__ = "FrameToStream"
        return wrapper

    @staticmethod
    def FrameToFrame(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.__type__ = "FrameToFrame"
        return wrapper

    @staticmethod
    def StreamToFrame(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.__type__ = "StreamToFrame"
        return wrapper

    @staticmethod
    def StreamToStream(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.__type__ = "StreamToStream"
        return wrapper
