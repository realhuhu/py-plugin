import io
from nonebot_plugin_imageutils import BuildImage


def BytesIOToBytes(_bytesIO: io.BytesIO) -> bytes:
    _bytesIO.seek(0)
    return _bytesIO.read()


def BytesToBuildImage(_bytes: bytes) -> BuildImage:
    return BuildImage.open(io.BytesIO(_bytes))
