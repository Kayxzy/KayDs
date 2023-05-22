import sys
from os import environ, execle

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.events import man_cmd


@man_cmd(pattern="restart$")
async def killdabot(event):
    await event.edit("**Multi-Userbot Berhasil di Restart**")
    args = [sys.executable, "-m", "userbot"]
    execle(sys.executable, *args, environ)


CMD_HELP.update(
    {
        "restart": f"**Plugin : **`restart`\
        \n\n  •  **Syntax :** `{cmd}restart`\
        \n  •  **Function : **Untuk Merestart userbot.\
    "
    }
)
