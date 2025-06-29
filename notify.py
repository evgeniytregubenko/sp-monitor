import os
from telegram import Bot

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID", None)  # добавим позже

bot = Bot(token=TELEGRAM_TOKEN)

def send_notification(message):
    if not CHAT_ID:
        print("CHAT_ID не указан!")
        return
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    send_notification("🎉 Бот успешно настроен и готов к работе!")
