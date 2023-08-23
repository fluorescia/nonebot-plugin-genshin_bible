from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from pathlib import Path
import random
from nonebot.rule import Rule
try:
    import ujson as json
except ModuleNotFoundError:
    import json

#enable_group = [123456789]
#async def checker_group(event: GroupMessageEvent) -> bool:
#    return True if event.group_id in enable_group else False


genshin_file = Path(__file__).parent / "genshin_bible.json"
genshin_dict = json.loads(genshin_file.read_text("utf-8"))
genshin_list = genshin_dict["genshin"]



#genshin = on_command("原神圣经", block = True , priority = 5, rule = Rule(checker_group))
genshin = on_command("原神圣经", aliases={"原神语录", "原神文案"}, block = True, priority = 5)
@genshin.handle()
async def _(event: GroupMessageEvent):
    await genshin.finish(random.choice(genshin_list))