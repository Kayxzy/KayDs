# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by @mrismanaziz
# @SharingUserbot

import asyncio

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.events import man_cmd


@man_cmd(
    pattern="f(typing|audio|contact|document|game|location|photo|round|sticker|video) ?(.*)",
)
async def _(e):
    act = e.pattern_match.group(1)
    t = e.pattern_match.group(2)
    if act in ["audio", "round", "video"]:
        act = "record-" + act
    t = int(t) if t.isdigit() else 60
    await e.edit(f"**Memulai Fake Action Selama** `{t}` **detik**")
    await asyncio.sleep(3)
    await e.delete()
    async with e.client.action(e.chat_id, act):
        await asyncio.sleep(t)


CMD_HELP.update(
    {
        "fakeaction": f"**Plugin :** `fakeaction`\
        \n\n  •  **Syntax :** `{cmd}ftyping`  <jumlah detik>\
        \n  •  **Function :** Menampilkan Pengetikan Palsu dalam obrolan\
        \n\n  •  **Syntax :** `{cmd}faudio` <jumlah detik>\
        \n  •  **Function :** Menampilkan Tindakan Merekam suara Palsu dalam obrolan\
        \n\n  •  **Syntax :** `{cmd}fvideo` <jumlah detik>\
        \n  •  **Function :** Menampilkan Tindakan Merekam Video Palsu dalam obrolan\
        \n\n  •  **Syntax :** `{cmd}fround` <jumlah detik>\
        \n  •  **Function :** Menampilkan Tindakan Merekam Live Video Round Palsu dalam obrolan\
        \n\n  •  **Syntax :** `{cmd}fgame` <jumlah detik>\
        \n  •  **Function :** Menampilkan sedang bermain game Palsu dalam obrolan\
        \n\n  •  **Syntax :** `{cmd}fphoto` <jumlah detik>\
        \n  •  **Function :** Menampilkan Tindakan Mengirim Photo Palsu dalam obrolan\
        \n\n  •  **Syntax :** `{cmd}fdocument` <jumlah detik>\
        \n  •  **Function :** Menampilkan Tindakan Mengirim Document/File Palsu dalam obrolan\
        \n\n  •  **Syntax :** `{cmd}flocation` <jumlah detik>\
        \n  •  **Function :** Menampilkan Tindakan Share Lokasi Palsu dalam obrolan\
        \n\n  •  **Syntax :** `{cmd}fcontact` <jumlah detik>\
        \n  •  **Function :** Menampilkan Tindakan Share Contact Palsu dalam obrolan\
    "
    }
)
