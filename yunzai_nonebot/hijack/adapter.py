from typing import Any

from nonebot import Bot, logger
from nonebot.adapters.onebot import V11Adapter, V12Adapter, V11Bot, V12Bot

from yunzai_nonebot.utils import AsyncMap, AsyncQueue, v11_to_request, result_to_v11, v12_to_request, result_to_v12
from .driver import GRPCDriver


class OneAdapter(V11Adapter, V12Adapter):
    def __init__(self, driver: GRPCDriver, **kwargs: Any):
        super().__init__(driver, **kwargs)

    @classmethod
    def get_name(cls) -> str:
        return "OneAdapter"

    async def _call_api(self, bot: Bot, api: str, **data: Any) -> Any:
        if api == "get_group_at_all_remain":
            return {
                "can_at_all": True,
                "remain_at_all_count_for_group": 100,
                "remain_at_all_count_for_uin": 100,
            }

        if isinstance(bot, V11Bot):
            request_type, request = v11_to_request(bot, api, **data)
            request_id = await AsyncQueue(bot.self_id).put(request_type, request)
            result = await AsyncMap(bot.self_id).get(request_id)
            if not result:
                logger.error(f"ob11获取result失败:{request_type}({request_id})")
                return None

            return result_to_v11(result)
        if isinstance(bot, V12Bot):
            request_type, request = v12_to_request(bot, api, **data)
            request_id = await AsyncQueue(bot.self_id).put(request_type, request)
            result = await AsyncMap(bot.self_id).get(request_id)
            if not result:
                logger.error(f"ob12获取result失败:{request_type}({request_id})")
                return None

            return result_to_v12(result)


def hijack_adapter():
    return OneAdapter
