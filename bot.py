import os
import telebot
import lyricsgenius

# Variables dan olish
BOT_TOKEN = os.getenv("8585168516:AAEdcJs-s2aEzZnOrZt88m7IExYw-F4Tv8w")
GENIUS_TOKEN = os.getenv("WMlTX_M4y4JAuBlG94yL7zqt5RFq5VnmVYNtNNSmE-99KA5PzMHI8VFmxBDOHBYM")

bot = telebot.TeleBot(BOT_TOKEN)
genius = lyricsgenius.Genius(GENIUS_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom! Musiqani nomini yozing va lyricsni oling.")

@bot.message_handler(func=lambda message: True)
def get_lyrics(message):
    song_name = message.text
    song = genius.search_song(song_name)
    if song:
        bot.send_message(message.chat.id, song.lyrics)
    else:
        bot.send_message(message.chat.id, "Lyrics topilmadi 😢")

bot.polling()
