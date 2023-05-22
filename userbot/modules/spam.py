import asyncio
from asyncio import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.events import man_cmd


@man_cmd(pattern="cspam (.+)")
async def tmeme(e):
    cspam = str(e.pattern_match.group(1))
    message = cspam.replace(" ", "")
    await e.delete()
    for letter in message:
        await e.respond(letter)


@man_cmd(pattern="wspam (.+)")
async def t_meme(e):
    wspam = str(e.pattern_match.group(1))
    message = wspam.split()
    await e.delete()
    for word in message:
        await e.respond(word)


@man_cmd(pattern="spam (\d+) (.+)")
async def spammer(e):
    counter = int(e.pattern_match.group(1))
    spam_message = str(e.pattern_match.group(2))
    await e.delete()
    await asyncio.wait([e.respond(spam_message) for i in range(counter)])


@man_cmd(pattern="picspam (\d+) (.+)")
async def tiny_pic_spam(e):
    counter = int(e.pattern_match.group(1))
    link = str(e.pattern_match.group(2))
    await e.delete()
    for _ in range(1, counter):
        await e.client.send_file(e.chat_id, link)


@man_cmd(pattern="delayspam (.*)")
async def spammer(e):
    spamDelay = float(e.pattern_match.group(1).split(" ", 2)[0])
    counter = int(e.pattern_match.group(1).split(" ", 2)[1])
    spam_message = str(e.pattern_match.group(1).split(" ", 2)[2])
    await e.delete()
    for _ in range(1, counter):
        await e.respond(spam_message)
        await sleep(spamDelay)


CMD_HELP.update(
    {
        "spam": f"**Plugin : **`spam`\
        \n\n  •  **Syntax :** `{cmd}spam` <jumlah spam> <text>\
        \n  •  **Function : **Membanjiri teks dalam obrolan!! \
        \n\n  •  **Syntax :** `{cmd}cspam` <text>\
        \n  •  **Function : **Spam surat teks dengan huruf. \
        \n\n  •  **Syntax :** `{cmd}wspam` <text>\
        \n  •  **Function : **Spam kata teks demi kata. \
        \n\n  •  **Syntax :** `{cmd}picspam` <jumlah spam> <link image/gif>\
        \n  •  **Function : **Spam Foto Seolah-olah spam teks tidak cukup !! \
        \n\n  •  **Syntax :** `{cmd}delayspam` <detik> <jumlah spam> <text>\
        \n  •  **Function : **Spam surat teks dengan huruf. \
        \n\n  •  **NOTE : Spam dengan Risiko Anda sendiri**\
    "
    }
)
