import time
import telegram
import random

bot_token = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"

assets = ["URUUSD"]
directions = ["🟢 UP", "🔴 DOWN"]

bot = telegram.Bot(token=bot_token)

def send_signal():
    asset = random.choice(assets)
    direction = random.choice(directions)
    signal = f"""
🧠 Quotex Signal
---------------------
🪙 Asset: {asset}
📈 Direction: {direction}
⏱️ Time: 1 Minute
💰 Confidence: High
---------------------
Wait for result...
"""
    bot.send_message(chat_id=chat_id, text=signal)
    time.sleep(60)
    result = random.choice(["✅ Win", "❌ Loss"])
    bot.send_message(chat_id=chat_id, text=f"📊 Result: {result}")

while True:
    send_signal()
    time.sleep(300)  # Every 5 minutes
