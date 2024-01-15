from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "6835125869:AAG2b1HTuDy9Ixq_wawdEyjhyeLelcn8xx0")

API_ID = int(os.environ.get("API_ID", "20919286"))

API_HASH = os.environ.get("API_HASH", "57b85f72104db3f08f9795b0410eb556")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
