import telebot

token = '7166707397:AAGVYvapB_wbBc2jcNt44Qb59xaf5JYDiHw'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")


bot.infinity_polling()
