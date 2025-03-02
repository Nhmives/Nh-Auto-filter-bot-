import threading
from server import app  # Import the Flask server
from your_bot_file import bot  # Import your bot instance

# Start the Flask server in a separate thread
threading.Thread(target=lambda: app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))).start()

# Start your Telegram bot
bot.run()
