import asyncio

from userbot import CMD_HELP
from userbot.events import man_cmd

modules = CMD_HELP


@man_cmd(pattern="help(?: |$)(.*)")
async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(f"`{args}` **Bukan Nama Modul yang Valid.**")
            await asyncio.sleep(15)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t\t|\t\t"
        await event.edit(
            f"**✦ Daftar Perintah Untuk Multi-Userbot:**\n\n"
            f"|  {string}"
            "\n\n**Contoh Ketik** `.help gcast` **Untuk Melihat Informasi Module**"
        )
