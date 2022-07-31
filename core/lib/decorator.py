class channel:
    @staticmethod
    def us(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.__channel_type__ = "UnaryToStream"
        return wrapper

    @staticmethod
    def uu(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.__channel_type__ = "UnaryToUnary"
        return wrapper

    @staticmethod
    def su(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.__channel_type__ = "StreamToUnary"
        return wrapper

    @staticmethod
    def ss(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.__channel_type__ = "StreamToStream"
        return wrapper
