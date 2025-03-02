import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNELS = os.getenv("CHANNELS", "-1002343295673").split()  # List of channel IDs
