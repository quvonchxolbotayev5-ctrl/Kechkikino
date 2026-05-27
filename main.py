import telebot
import os
from flask import Flask
from threading import Thread

# Bot Token va Admin ID
TOKEN = "8893738423:AAEpRdwSajEG8Ye4xpmnqjHHUlVaYWGQFIg"
ADMIN_ID = 6352602211
bot = telebot.TeleBot(TOKEN)

# 24/7 ishlashi uchun veb-server
app = Flask('')
@app.route('/')
def home(): return "Bot is running!"

def run(): app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Bot kodi
movies = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot ishga tushdi! Kino kodini yuboring.")

@bot.message_handler(content_types=['video'])
def add(message):
    if message.from_user.id == ADMIN_ID and message.caption:
        movies[message.caption] = message.video.file_id
        bot.reply_to(message, f"Saqlandi! Link: t.me/{bot.get_me().username}?start={message.caption}")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()

