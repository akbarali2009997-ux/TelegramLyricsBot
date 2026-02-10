import telebot
import lyricsgenius

# =============================
# Bu yerga tokenlaringizni kiriting
# =============================
BOT_TOKEN = "8585168516:AAEdcJs-s2aEzZnOrZt88m7IExYw-F4Tv8w"
GENIUS_TOKEN = "WMlTX_M4y4JAuBlG94yL7zqt5RFq5VnmVYNtNNSmE-99KA5PzMHI8VFmxBDOHBYM"

bot = telebot.TeleBot(BOT_TOKEN)
genius = lyricsgenius.Genius(GENIUS_TOKEN)

# =============================
# /start komandasi
# =============================
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Musiqaning nomini yozing, men sizga lyricsini topib beraman 🎵")

# =============================
# Foydalanuvchi nom yozganda
# =============================
@bot.message_handler(func=lambda message: True)
def get_lyrics(message):
    song_name = message.text
    try:
        song = genius.search_song(song_name)
        if song and song.lyrics:
            # Agar lyrics uzun bo‘lsa, bo‘laklarga ajratib yuborish tavsiya qilinadi
            for chunk in [song.lyrics[i:i+4000] for i in range(0, len(song.lyrics), 4000)]:
                bot.send_message(message.chat.id, chunk)
        else:
            bot.reply_to(message, "Lyrics topilmadi 😢")
    except Exception as e:
        bot.reply_to(message, f"Xatolik yuz berdi: {e}")

# =============================
# Botni ishga tushirish
# =============================
bot.polling()
