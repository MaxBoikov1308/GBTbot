import telebot
from telebot import types
from db.registration import add_email, add_password, add_tg_id


token = '7166707397:AAGVYvapB_wbBc2jcNt44Qb59xaf5JYDiHw'
bot = telebot.TeleBot(token)
HELP_MESSAGE = """commands:
⚪ /help - show available commands
⚪ /gpt - run gpt
⚪ /register - register in bot
⚪ /restart - restart bot
"""


@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1 = types.KeyboardButton('/gpt')
  markup.add(item1)
  bot.send_message(message.chat.id, 'Choose the option', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP_MESSAGE)

@bot.message_handler(commands=['gpt'])
def gpt(message):
    bot.send_message(message.chat.id, 'Type your request')
    bot.register_next_step_handler(message, reply)
    
def reply(message):  # this will be reply from gpt
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(commands=["restart"])
def restart(message):
    bot.register_next_step_handler(message, start)

@bot.message_handler(commands=["register"])
def start_registration(message):
    bot.send_message(message.chat.id, "enter your email and password for registration")
    bot.send_message(message.chat.id, "enter email")
    bot.register_next_step_handler(message, username)

def username(message):
    email = message.text
    if "@" not in email:
        bot.send_message(message.chat.id, "email must contains @, try again")
        bot.register_next_step_handler(message, username)
    else:
        add_email(email)
        bot.send_message(message.chat.id, "email successfully added!")
        bot.send_message(message.chat.id, "enter password")
        bot.register_next_step_handler(message, password)

def password(message):
    password = message.text
    add_password(password)
    bot.send_message(message.chat.id, "you successfully registred!")

bot.infinity_polling()
