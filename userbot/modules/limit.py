from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.events import man_cmd


@man_cmd(pattern="limit(?: |$)(.*)")
async def _(event):
    await event.edit("`Processing...`")
    async with event.client.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("**Mohon Unblock @SpamBot dan coba lagi**")
            return
        await event.edit(f"~ {response.message.message}")


CMD_HELP.update(
    {
        "limit": f"**Plugin : **`limit`\
        \n\n  •  **Syntax :** `{cmd}limit`\
        \n  •  **Function : **Untuk Mengecek akun anda sedang terkena limit atau tidak dengan menggunakan @spambot.\
    "
    }
)
