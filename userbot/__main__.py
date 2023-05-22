import sys
from importlib import import_module

from userbot import (
    LOGS,
    MAN2,
    MAN3,
    MAN4,
    MAN5,
    MAN6,
    MAN7,
    MAN8,
    MAN9,
    MAN10,
    STRING_1,
    STRING_2,
    STRING_3,
    STRING_4,
    STRING_5,
    STRING_6,
    STRING_7,
    STRING_8,
    STRING_9,
    STRING_10,
    bot,
)
from userbot.modules import ALL_MODULES

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)


# Multi-Client helper
async def man_client(client):
    client.me = await client.get_me()
    client.uid = telethon.utils.get_peer_id(client.me)


# Multi-Client Starter
def multiman():
    if STRING_1:
        LOGS.info("STRING_1 detected! Starting 1st Client.")
        try:
            bot.start()
            bot.loop.run_until_complete(man_client(bot))
        except Exception as e:
            print(e)
    else:
        LOGS.info("STRING_1 Not Found")

    if STRING_2:
        LOGS.info("STRING_2 detected! Starting 2nd Client.")
        try:
            MAN2.start()
            MAN2.loop.run_until_complete(man_client(MAN2))
        except Exception as e:
            print(e)
    else:
        LOGS.info("STRING_2 Not Found")

    if STRING_3:
        LOGS.info("STRING_3 detected! Starting 3rd Client.")
        try:
            MAN3.start()
            MAN3.loop.run_until_complete(man_client(MAN3))
        except Exception as e:
            print(e)
    else:
        LOGS.info("STRING_3 Not Found")

    if STRING_4:
        LOGS.info("STRING_4 detected! Starting 4th Client.")
        try:
            MAN4.start()
            MAN4.loop.run_until_complete(man_client(MAN4))
        except Exception as e:
            print(e)
    else:
        LOGS.info("STRING_4 Not Found")

    if STRING_5:
        LOGS.info("STRING_5 detected! Starting 5th Client.")
        try:
            MAN5.start()
            MAN5.loop.run_until_complete(man_client(MAN5))
        except Exception as e:
            print(e)
    else:
        LOGS.info("STRING_5 Not Found")

    if STRING_6:
        LOGS.info("STRING_6 detected! Starting 6th Client.")
        try:
            MAN6.start()
            MAN6.loop.run_until_complete(man_client(MAN6))
        except Exception as e:
            print(e)
    else:
        LOGS.info("STRING_6 Not Found")

    if STRING_7:
        LOGS.info("STRING_7 detected! Starting 7th Client.")
        try:
            MAN7.start()
            MAN7.loop.run_until_complete(man_client(MAN7))
        except Exception as e:
            print(e)
    else:
        LOGS.info("STRING_7 Not Found")

    if STRING_8:
        LOGS.info("STRING_8 detected! Starting 8th Client.")
        try:
            MAN8.start()
            MAN8.loop.run_until_complete(man_client(MAN8))
        except Exception as e:
            print(e)
    else:
        LOGS.info("STRING_8 Not Found")

    if STRING_9:
        LOGS.info("STRING_9 detected! Starting 9th Client.")
        try:
            MAN9.start()
            MAN9.loop.run_until_complete(man_client(MAN9))
        except Exception as e:
            print(e)
    else:
        LOGS.info("STRING_9 Not Found")

    if STRING_10:
        LOGS.info("STRING_10 detected! Starting 10th Client.")
        try:
            MAN10.start()
            MAN10.loop.run_until_complete(man_client(MAN10))
        except Exception as e:
            print(e)
    else:
        LOGS.info("STRING_10 Not Found")


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        client = multiman()
        LOGS.info("Multi-Userbot ⚙️ [🔥 BERHASIL DIAKTIFKAN! 🔥]")
    except Exception as e:
        LOGS.error(str(e), exc_info=True)
        sys.exit()


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
