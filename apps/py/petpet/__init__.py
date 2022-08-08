from core import Handler, Request, Response, BytesIOToBytes, BytesToBuildImage
from .functions import *
from .download import download_avatar

import io

package = "petpet"


@Handler.FrameToFrame
async def _universal(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = universal(BytesToBuildImage(bytes_img), [request.message])
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _petpet(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    arg = "圆" if "圆" in request.event.msg else "方"
    image = petpet(BytesToBuildImage(bytes_img), arg)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _kiss(request: Request) -> Response:
    sender_img = BytesToBuildImage(await download_avatar(request.event.sender.qq))
    if len(request.event.imageList) >= 2:
        img_list = [
            BytesToBuildImage(request.event.imageList[0]),
            BytesToBuildImage(request.event.imageList[1])
        ]
    else:
        if request.event.imageList:
            img_list = [BytesToBuildImage(request.event.imageList[0])]
        elif request.event.atList:
            img_list = [BytesToBuildImage(await download_avatar(request.event.atList[0].qq))]
        else:
            img_list = [sender_img]

    image = kiss(img_list, sender_img)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _rub(request: Request) -> Response:
    sender_img = BytesToBuildImage(await download_avatar(request.event.sender.qq))

    if len(request.event.imageList) >= 2:
        img_list = [
            BytesToBuildImage(request.event.imageList[0]),
            BytesToBuildImage(request.event.imageList[1])
        ]
    else:
        if request.event.imageList:
            img_list = [BytesToBuildImage(request.event.imageList[0])]
        elif request.event.atList:
            img_list = [BytesToBuildImage(await download_avatar(request.event.atList[0].qq))]
        else:
            img_list = [sender_img]

    image = rub(img_list, sender_img)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _play(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = play(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _pat(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = pat(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _rip(request: Request) -> Response:
    img_list = [BytesToBuildImage(await download_avatar(request.event.sender.qq))]

    if request.event.imageList:
        img_list += [BytesToBuildImage(request.event.imageList[0])]
    elif request.event.atList:
        img_list += [BytesToBuildImage(await download_avatar(request.event.atList[0].qq))]
    else:
        pass

    image = rip(img_list)

    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _throw(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = throw(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _crawl(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = crawl(BytesToBuildImage(bytes_img), request.event.msg.replace("爬", ""))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _support(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = support(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _always(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = always(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _loading(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = loading(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _dont_touch(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = dont_touch(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _alike(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = alike(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _roll(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = roll(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _play_game(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = play_game(BytesToBuildImage(bytes_img), request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _worship(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = worship(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _eat(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = eat(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _bite(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = bite(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _police(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = police(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _police1(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = police1(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _prpr(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = prpr(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _twist(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = twist(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _wallpaper(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = wallpaper(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _china_flag(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = china_flag(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _back_to_work(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = back_to_work(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _perfect(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = perfect(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _paint(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = paint(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _listen_music(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = listen_music(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _funny_mirror(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = funny_mirror(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _love_you(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = love_you(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _symmetric(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = symmetric(BytesToBuildImage(bytes_img), request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _interview(request: Request) -> Response:
    sender_img = BytesToBuildImage(await download_avatar(request.event.sender.qq))

    if len(request.event.imageList) >= 2:
        img_list = [
            BytesToBuildImage(request.event.imageList[0]),
            BytesToBuildImage(request.event.imageList[1])
        ]
    else:
        if request.event.imageList:
            img_list = [BytesToBuildImage(request.event.imageList[0])]
        elif request.event.atList:
            img_list = [BytesToBuildImage(await download_avatar(request.event.atList[0].qq))]
        else:
            img_list = [sender_img]

    image = interview(img_list, request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _punch(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = punch(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _cyan(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = cyan(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _pound(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = pound(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _thump(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = thump(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _need(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = need(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _cover_face(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = cover_face(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _cover_face(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = cover_face(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _knock(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = knock(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _knock(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = knock(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _garbage(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = garbage(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _whyatme(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = whyatme(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _decent_kiss(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = decent_kiss(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _jiujiu(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = jiujiu(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _suck(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = suck(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _hammer(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = hammer(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _tightly(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = tightly(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _distracted(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = distracted(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _anyasuki(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = anyasuki(BytesToBuildImage(bytes_img), request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _thinkwhat(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = thinkwhat(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _keepaway(request: Request) -> Response:
    imageList = []
    for i in request.event.imageList:
        imageList.append(BytesToBuildImage(i))
    for i in request.event.atList:
        imageList.append(BytesToBuildImage(await download_avatar(i.qq)))

    image = keepaway(imageList, request.message)
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _marriage(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = marriage(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _painter(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = painter(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _anti_kidnap(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = anti_kidnap(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))


@Handler.FrameToFrame
async def _charpic(request: Request) -> Response:
    if request.event.imageList:
        bytes_img = request.event.imageList[0]
    elif request.event.atList:
        bytes_img = await download_avatar(request.event.atList[0].qq)
    else:
        bytes_img = await download_avatar(request.event.sender.qq)

    image = charpic(BytesToBuildImage(bytes_img))
    return Response(image=BytesIOToBytes(image))
