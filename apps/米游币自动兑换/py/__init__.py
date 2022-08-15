import re
from .data_source import get_address, get_goods, save_exchange_info, get_exchange_info, delete_exchange_info
from core import Handler, RequestIterator, ResponseIterator, Response, Request

package = "myb"


@Handler.StreamToStream
async def myb_add(request_iterator: RequestIterator) -> ResponseIterator:
    state = {}

    yield Response("请给出要抢的商品类型(虚拟|实体)，例如原石属于虚拟")

    while True:
        request = await request_iterator.__anext__()

        if '虚拟' in request.event.msg:
            state['商品类型'] = '虚拟'
            break
        elif '实体' in request.event.msg:
            state['商品类型'] = '实体'
            state['uid'] = None
            break
        else:
            yield Response("无效的商品类型")

    if state['商品类型'] == '虚拟':
        yield Response("请把虚拟商品要兑换到的游戏uid告诉我")
        while True:
            request = await request_iterator.__anext__()

            find_uid = re.search(r'(?P<uid>(1|2|5)\d{8})', request.event.msg)
            if find_uid:
                state['uid'] = find_uid.group('uid')
                break
            else:
                yield Response('这不是有效的uid')

    yield Response("请把米游社cookie给我")

    while True:
        request = await request_iterator.__anext__()

        cookie = request.event.msg
        address = await get_address(cookie)
        if address is None:
            yield Response('这个cookie无效，请检查是否以按照正常方法获取')
        elif len(address) == 0:
            yield Response('你的账号还没有填写收货地址哦，请先去 米游社手机版>我的>右上角设置>通行证与账号安全>管理收货地址 填写收货地址重新再来')
        else:
            state['cookie'] = cookie
            if len(address) == 1:
                state['address_id'] = address[0]
            else:
                state['address_list'] = address

            if state['商品类型'] == '虚拟':
                if 'login_ticket' not in cookie and 'stoken' not in cookie:
                    yield Response('你的cookie中没有login_ticket字段哦，请尝试退出后重新登录再获取cookie')
                else:
                    break
            else:
                break

    if not state.get("address_id"):
        address_list = []
        for add in state['address_list']:
            address_list += f'ID：{add["id"]}，{add["地址"]}\n'

        yield Response(f"请选择你的收货地址的ID\n{address_list}")

        while True:
            request = await request_iterator.__anext__()
            address_id = request.event.msg
            flag = False
            for add in state['address_list']:
                if address_id == add["id"]:
                    state['address_id'] = add
                    flag = True
                    break

            if flag:
                break
            else:
                yield Response('没有找到该地址，请确认后重新发送地址ID')

    yield Response(f"收货地址:{state['address_id']['地址']}")

    while True:
        yield Response(f"请给出要抢的商品所属游戏名称，有崩坏3|原神|崩坏学园2|未定事件簿|米游社")
        request = await request_iterator.__anext__()
        game = request.event.msg
        if game in ['崩坏3', 'bh3', '崩崩崩', '三崩子']:
            state['goods_list'] = await get_goods('崩坏3')
            break
        elif game in ['原神', 'ys']:
            state['goods_list'] = await get_goods('原神')
            break
        elif game in ['崩坏学园2', 'bh2', '二崩子', '崩坏学院2', '崩崩']:
            state['goods_list'] = await get_goods('崩坏学园2')
            break
        elif game in ['未定事件簿', 'wdsjb', '未定']:
            state['goods_list'] = await get_goods('未定事件簿')
            break
        elif game in ['米游社', 'mys']:
            state['goods_list'] = await get_goods('米游社')
            break

    yield Response(f"请给出要兑换的商品名，或者其含有的关键词")

    while True:
        request = await request_iterator.__anext__()
        goods_search = request.event.msg
        match_goods = []
        for good in state['goods_list']:
            if goods_search in good['name']:
                match_goods.append(good)

        if len(match_goods) == 1:
            state['goods'] = match_goods[0]
            save_exchange_info(request.event.sender.qq, state)
            yield Response(
                '兑换计划录入成功，发送 #我的米游币任务 可以再次确认兑换信息，发送 #删除米游币任务 可以取消兑换计划',
                messageDict={"stop": "true"}
            )
            break
        elif len(match_goods) > 1:
            state['goods_search_result'] = match_goods
            break
        else:
            yield Response('没有相关可兑换的商品，请重新输入')

    if not state.get("goods"):
        goods_list = ""
        for goods in state['goods_search_result']:
            goods_list += f'ID：{goods["id"]}，{goods["name"]}\n'

        yield Response(f"请选择物品ID\n{goods_list}")

        while True:
            request = await request_iterator.__anext__()
            msg = request.event.msg

            flag = False
            for good in state['goods_search_result']:
                if msg == good['id']:
                    state['goods'] = good
                    save_exchange_info(request.event.sender.qq, state)
                    flag = True
                    yield Response(
                        '兑换计划录入成功，发送 #我的米游币任务 可以再次确认兑换信息，发送 #删除米游币任务 可以取消兑换计划',
                        messageDict={"stop": "true"}
                    )
                    break

            if flag:
                break
            else:
                yield Response('没有找到商品，请确认后重新发送商品ID')


@Handler.FrameToFrame
async def myb_show(request: Request) -> Response:
    info = get_exchange_info(request.event.sender.qq)
    return Response(info)


@Handler.FrameToFrame
async def myb_cancel(request: Request) -> Response:
    if delete_exchange_info(request.event.sender.qq, request.message):
        return Response(f"米游币兑换计划{request.message}已取消,剩余计划:\n{get_exchange_info(request.event.sender.qq)}")
    else:
        return Response(f"找不到该计划米游币兑换计划,全部计划:\n{get_exchange_info(request.event.sender.qq)}")


