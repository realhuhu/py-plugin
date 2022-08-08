import { FrameToFrame, createEvent } from "../../core/client/client.js";
import { segment } from "oicq";

export const rule = {
  petpet: {
    reg: "noCheck",
    priority: 800,
    describe: "表情制作",
  },
};

const pattern = [
  { regex: /^(万能|空白)表情/g, handler: "_universal" },
  { regex: /^(摸摸?头?|rua)圆?$/g, handler: "_petpet" },
  { regex: /^亲亲?$/g, handler: "_kiss" },
  { regex: /^贴贴?|蹭蹭?$/g, handler: "_rub" },
  { regex: /^顶|玩$/g, handler: "_play" },
  { regex: /^拍$/g, handler: "_pat" },
  { regex: /^撕$/g, handler: "_rip" },
  { regex: /^丢|扔$/g, handler: "_throw" },
  { regex: /^爬([0-9]+)?$/g, handler: "_crawl" },
  { regex: /^精神支柱$/g, handler: "_support" },
  { regex: /^一直$/g, handler: "_always" },
  { regex: /^加载中$/g, handler: "_loading" },
  { regex: /^转$/g, handler: "_turn" },
  // { regex: /^小天使$/g, handler: "_littleangel" },
  { regex: /^不要靠近$/g, handler: "_dont_touch" },
  { regex: /^一样$/g, handler: "_alike" },
  { regex: /^滚$/g, handler: "_roll" },
  { regex: /^来?玩游戏/g, handler: "_play_game" },
  { regex: /^膜拜$/g, handler: "_worship" },
  { regex: /^吃$/g, handler: "_eat" },
  { regex: /^啃$/g, handler: "_bite" },
  { regex: /^出警$/g, handler: "_police" },
  { regex: /^警察$/g, handler: "_police1" },
  // { regex: /^去?问问$?/g, handler: "_ask" },
  { regex: /^舔屏|prpr$/g, handler: "_prpr" },
  { regex: /^搓$/g, handler: "_twist" },
  { regex: /^墙纸$/g, handler: "_wallpaper" },
  { regex: /^国旗$/g, handler: "_china_flag" },
  // { regex: /^交个朋友$?/g, handler: "_make_friend" },
  { regex: /^继续干活|打工人$/g, handler: "_back_to_work" },
  { regex: /^完美的?$/g, handler: "_perfect" },
  // { regex: /^关注$/g, handler: "_follow" },
  // { regex: /^我朋友说$/g, handler: "_my_friend" },
  { regex: /^这像画吗$/g, handler: "_paint" },
  // { regex: /^兑换券?$/g, handler: "_coupon" },
  { regex: /^听音乐$/g, handler: "_listen_music" },
  { regex: /^哈哈镜$/g, handler: "_funny_mirror" },
  { regex: /^永远爱你$/g, handler: "_love_you" },
  { regex: /^对称[上下左右]?$/g, handler: "_symmetric" },
  // { regex: /^安全感$/g, handler: "_safe_sense" },
  // { regex: /^我?永远喜欢$/g, handler: "_always_like" },
  { regex: /^采访/g, handler: "_interview" },
  { regex: /^打拳$/g, handler: "_punch" },
  { regex: /^群青$/g, handler: "_cyan" },
  { regex: /^捣$/g, handler: "_pound" },
  { regex: /^捶$/g, handler: "_thump" },
  { regex: /^需要|你可能需要$/g, handler: "_need" },
  { regex: /^捂脸$/g, handler: "_cover_face" },
  { regex: /^垃圾桶?$/g, handler: "_garbage" },
  { regex: /^为什么(?:@|at)我$/g, handler: "_whyatme" },
  { regex: /^像样的亲亲$/g, handler: "_decent_kiss" },
  { regex: /^啾啾$/g, handler: "_jiujiu" },
  { regex: /^吸|嗦$/g, handler: "_suck" },
  { regex: /^锤$/g, handler: "_hammer" },
  { regex: /^紧贴|紧紧贴着$/g, handler: "_tightly" },
  { regex: /^注意力涣散$/g, handler: "_distracted" },
  { regex: /^阿尼亚喜欢/g, handler: "_anyasuki" },
  { regex: /^想什么$/g, handler: "_thinkwhat" },
  { regex: /^远离$/g, handler: "_keepaway" },
  { regex: /^结婚申请$/g, handler: "_marriage" },
  { regex: /^小画家$/g, handler: "_painter" },
  // { regex: /^复读$/g, handler: "_repeat" },
  { regex: /^防诱拐$/g, handler: "_anti_kidnap" },
  { regex: /^字符画$/g, handler: "_charpic" },
  // { regex: /^这是我的老婆$/g, handler: "_mywife" },
];


export async function petpet(e) {
  let handler, message;

  for (let i of pattern) {
    if (i.regex.test(e.msg)) {
      handler = i.handler;
      message = e.msg.replace(i.regex, "");
      break;
    }
  }

  if (!handler) return;

  FrameToFrame({
    _package: "petpet",
    _handler: handler,
    params: {
      event: await createEvent(e),
      message: message,
    },
    onData: (error, response) => {
      if (error) {
        console.error(error.details);
      } else {
        e.reply(segment.image(response.image));
      }
    },
  });

  return true;
}