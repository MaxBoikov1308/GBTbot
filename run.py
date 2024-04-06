import telebot
from telebot import types

token = '7166707397:AAGVYvapB_wbBc2jcNt44Qb59xaf5JYDiHw'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def button_message(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1 = types.KeyboardButton('GPT')
  item2 = types.KeyboardButton('Help')
  markup.add(item1)
  markup.add(item2)
  bot.send_message(message.chat.id, 'Choose the option', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, help_message())

def help_message():
    return 'Comamnds: /help - show available commands'

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "GPT4":  # it will be GPT question and answer
        bot.send_message(message.chat.id, GPT())
    elif message.text == "Help":
        bot.send_message(message.chat.id, help_message())

def GPT(question=""):
    return "answer"

bot.infinity_polling()
