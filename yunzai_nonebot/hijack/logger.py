import re
import sys

from nonebot.log import logger


def default_filter(record):
    record["name"] = re.sub(
        "(nonebot_plugin_|yunzai_nonebot.hijack.|yunzai_nonebot.utils.|nonebot.)",
        "",
        record["name"]
    )
    record["name"] = re.sub(".*onebot.v1[12].", "onebot", record["name"])

    if record["name"] in ["internal.matcher.matcher"] and not record["extra"].get("independent"):
        return False
    if "OneAdapter" in record["message"] and not record["extra"].get("independent"):
        return False
    record["message"] = record["message"].replace("Event will be handled by", " 触发")
    log_level = record["extra"].get("log_level", "INFO")
    levelno = logger.level(log_level).no if isinstance(log_level, str) else log_level
    return record["level"].no >= levelno


default_format: str = (
    "[PyBot]"
    "[<g>{time:HH:mm:ss.SSS}</g>]"
    "[<lvl>{level}</lvl>] "
    "[<c><u>{name}</u></c>]"
    "{message}"
)


def hijack_logger():
    logger.remove()
    logger.add(
        sys.stdout,
        level=0,
        diagnose=False,
        filter=default_filter,
        format=default_format,
    )
