import telebot
from telebot import types
from telegram import User, Update


token = '7166707397:AAGVYvapB_wbBc2jcNt44Qb59xaf5JYDiHw'
bot = telebot.TeleBot(token)
HELP_MESSAGE = """commands:
⚪ /help - show available commands
⚪ /gpt - run gpt
"""


@bot.message_handler(commands=['start'])
def button_message(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1 = types.KeyboardButton('/gpt')
  item2 = types.KeyboardButton('/help')
  markup.add(item1)
  markup.add(item2)
  bot.send_message(message.chat.id, 'Choose the option', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP_MESSAGE)

@bot.message_handler(commands=['gpt'])
def gpt(message):
    bot.send_message(message.chat.id, 'Type your request')
    bot.register_next_step_handler(message, reply)
    
def reply(message):
    bot.send_message(message.chat.id, message.text)
    

def username(message):
    bot.register_next_step_handler(message, password)

def password(message):
    pass

bot.infinity_polling()
