import logging
import os
import sys
import time
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger
from sys import version_info

from dotenv import load_dotenv
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

load_dotenv("config.env")

StartTime = time.time()

# Bot Logs setup:
logging.basicConfig(
    format="[%(name)s] - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)
logging.getLogger("asyncio").setLevel(logging.ERROR)
logging.getLogger("telethon.network.mtprotosender").setLevel(logging.ERROR)
logging.getLogger("telethon.network.connection.connection").setLevel(logging.ERROR)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 9:
    LOGS.info(
        "Anda HARUS memiliki python setidaknya versi 3.9."
        "Beberapa fitur tergantung versi python ini. Bot berhenti."
    )
    sys.exit(1)

# Global Variables
CMD_HELP = {}
CMD_LIST = {}
SUDO_LIST = {}
LOAD_PLUG = {}

# Telegram App KEY and HASH
API_KEY = int(os.environ.get("API_KEY") or 0)
API_HASH = str(os.environ.get("API_HASH") or None)

# Userbot Session String
STRING_1 = os.environ.get("STRING_1", None)
STRING_2 = os.environ.get("STRING_2", None)
STRING_3 = os.environ.get("STRING_3", None)
STRING_4 = os.environ.get("STRING_4", None)
STRING_5 = os.environ.get("STRING_5", None)
STRING_6 = os.environ.get("STRING_6", None)
STRING_7 = os.environ.get("STRING_7", None)
STRING_8 = os.environ.get("STRING_8", None)
STRING_9 = os.environ.get("STRING_9", None)
STRING_10 = os.environ.get("STRING_10", None)

# Handler
CMD_HANDLER = os.environ.get("CMD_HANDLER") or "."
SUDO_HANDLER = os.environ.get("SUDO_HANDLER", r"$")
SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
BL_CHAT = {int(x) for x in os.environ.get("BL_CHAT", "").split()}

# Heroku
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)


if STRING_1:
    session = StringSession(str(STRING_1))
    bot = TelegramClient(
        session=session,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    bot = None


if STRING_2:
    session2 = StringSession(str(STRING_2))
    MAN2 = TelegramClient(
        session=session2,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    MAN2 = None


if STRING_3:
    session3 = StringSession(str(STRING_3))
    MAN3 = TelegramClient(
        session=session3,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    MAN3 = None


if STRING_4:
    session4 = StringSession(str(STRING_4))
    MAN4 = TelegramClient(
        session=session4,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    MAN4 = None


if STRING_5:
    session5 = StringSession(str(STRING_5))
    MAN5 = TelegramClient(
        session=session5,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    MAN5 = None


if STRING_6:
    session6 = StringSession(str(STRING_6))
    MAN6 = TelegramClient(
        session=session6,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    MAN6 = None


if STRING_7:
    session7 = StringSession(str(STRING_7))
    MAN7 = TelegramClient(
        session=session7,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    MAN7 = None


if STRING_8:
    session8 = StringSession(str(STRING_8))
    MAN8 = TelegramClient(
        session=session8,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    MAN8 = None


if STRING_9:
    session9 = StringSession(str(STRING_9))
    MAN9 = TelegramClient(
        session=session9,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    MAN9 = None


if STRING_10:
    session10 = StringSession(str(STRING_10))
    MAN10 = TelegramClient(
        session=session10,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    MAN10 = None
