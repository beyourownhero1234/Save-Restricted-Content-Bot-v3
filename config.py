# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """https://curl.haxx.se/rfc/cookie_spec.html"""

API_ID = os.getenv("API_ID", "20870930")
API_HASH = os.getenv("API_HASH", "d8339c188abe7b852e52ef2d0d48c770")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7829620390:AAEzxmpvsySkoPVWBTlx7SN5ZpvErUa6gGc")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://beyourownhero1234:UOGGpKz1jOBbIXeK@cluster0.xdwhfk0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "1760032652").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002308118349")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1002217595765")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "10"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "1000000000000000"))
