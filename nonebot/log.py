# Done TODO
import re
import sys
import logging

import loguru

logger = loguru.logger


class LoguruHandler(logging.Handler):  # pragma: no cover
    """logging 与 loguru 之间的桥梁，将 logging 的日志转发到 loguru。"""

    def emit(self, record: logging.LogRecord):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def default_filter(record):
    record["name"] = re.sub("(nonebot.|nonebot_plugin_)", "", record["name"])
    record["name"] = re.sub(".*onebot.v11.", "onebot", record["name"])
    log_level = record["extra"].get("nonebot_log_level", "INFO")
    levelno = logger.level(log_level).no if isinstance(log_level, str) else log_level
    return record["level"].no >= levelno


default_format: str = (
    "[PyBot]"
    "[<g>{time:HH:mm:ss.SSS}</g>]"
    "[<lvl>{level}</lvl>] "
    "[<c><u>{name}</u></c>]"
    "{message}"
)

logger.remove()
logger_id = logger.add(
    sys.stdout,
    level=0,
    diagnose=False,
    filter=default_filter,
    format=default_format,
)
