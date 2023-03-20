import telebot
import os

token = os.getenv("BOT_TOKEN", "!!")
if token != "!!":
    print(token)
    bot = telebot.TeleBot(token)
else:
    raise NameError

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "WIP")


bot.polling(none_stop=True, interval=0)
