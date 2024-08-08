# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29969211"))
API_HASH = getenv("API_HASH", "8e5d10aa4cc7b8952b1ad931a03e2e20")
BOT_TOKEN = getenv("BOT_TOKEN", "7288656783:AAGdU4PzYU_-koPrMIuhJZzZJ-mtgXArznE")
OWNER_ID = int(getenv("OWNER_ID", "7285043138"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "")
LOG_GROUP = int(getenv("LOG_GROUP", "https://t.me/sdfsdfasdfwefewfwe/3-100"))
FORCESUB = getenv("FORCESUB", "sdfsdfasdfwefewfwe")
