import os
import logging
from pyrogram import Client, filters

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load API credentials from environment variables
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNELS = os.getenv("CHANNELS", "").split()  # List of channel IDs

bot = Client("AutoFilterBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.private & filters.text)
async def auto_filter(client, message):
    query = message.text.lower()
    
    for channel in CHANNELS:
        async for msg in client.search_messages(int(channel), query):
            if msg.document or msg.video or msg.audio:
                await message.reply_text(f"📂 **{msg.caption or 'File'}**\n👉 {msg.link}")
                return

    await message.reply_text("❌ No matching files found.")

if __name__ == "__main__":
    bot.run()
