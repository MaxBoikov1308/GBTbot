from telebot import TeleBot, types
# from database.dbapi import DatabaseConnector
from app import GPT
from interface import Interface


commands = ["/help", "/reg", "/gpt"]
versions = ["gpt-3.5-turbo", "gpt-4"]


class TelegramBot:

    def commands_keyboard(self, commands: list, versions: list, ischoose: bool = False, isgpt: bool = False, isreg: bool = False, islang: bool = False) -> types.InlineKeyboardMarkup:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        if ischoose:
            for version in versions:
                markup.add(types.KeyboardButton(version))
        elif isgpt:
            markup.add(types.KeyboardButton('/exit'))
        elif islang:
            markup.add(types.KeyboardButton('🇷🇺Русский'))
            markup.add(types.KeyboardButton('🇬🇧English'))
        else:
            for command in commands:
                markup.add(types.KeyboardButton(command))

        return markup

    def __init__(self, api_token: str) -> None:
        self.bot = TeleBot(api_token)
        self.handlers()
        self.gpt = GPT()
        self.lang = "🇬🇧English"
        self.interface = Interface()

    
    def handlers(self):
        
        @self.bot.message_handler(commands=['start'])
        def select_language(message) -> None:
            self.bot.send_message(message.chat.id, f"Choose language:\n",
                                  reply_markup=self.commands_keyboard(commands, versions, islang=True))
            self.bot.register_next_step_handler(message, start)
        
        def start(message) -> None:
            self.lang = message.text
            self.bot.send_message(message.chat.id, f"{self.interface.phrases('Welcome to the chatgpt_bot', self.lang)}, @{message.from_user.username}.\n"
                                            f"{self.interface.phrases('The following commands are available', self.lang)}:\n\n"
                                            f"{self.interface.phrases('/help - show available commands', self.lang)}\n"
                                            f"{self.interface.phrases('/gpt - run gpt', self.lang)}\n\n"
                                            f"@GPT_YandLms_bot", reply_markup=self.commands_keyboard(commands, versions))

        @self.bot.message_handler(commands=['help'])
        def help_message(message) -> None:
            self.bot.send_message(message.chat.id, f"{self.interface.phrases('The following commands are available', self.lang)}:\n\n"
                                            f"{self.interface.phrases('/help - show available commands', self.lang)}\n"
                                            f"{self.interface.phrases('/gpt - run gpt', self.lang)}\n\n"
                                            f"@GPT_YandLms_bot", reply_markup=self.commands_keyboard(commands, versions))
        
        @self.bot.message_handler(commands=['gpt'])
        def gpt(message) -> None:
            self.bot.send_message(message.chat.id, f"{self.interface.phrases('Choose GPT version', self.lang)}:\n",
                                  reply_markup=self.commands_keyboard(commands, versions, True))
            self.bot.register_next_step_handler(message, choose_version)
        
        def choose_version(message):
            try:
                version = message.text
                if version not in versions:
                    self.bot.send_message(message.chat.id, f"{self.interface.phrases('Choose correct version', self.lang)}",
                                        reply_markup=self.commands_keyboard(commands, versions, True))
                    self.bot.register_next_step_handler(message, choose_version)
                    return
                self.bot.reply_to(message, f"{self.interface.phrases('You chose', self.lang)}: {version}",
                                    reply_markup=self.commands_keyboard(commands, versions))
                self.bot.send_message(message.chat.id, f"{self.interface.phrases('Enter your request', self.lang)}: ",
                                        reply_markup=self.commands_keyboard(commands, versions, isgpt=True))
                self.bot.register_next_step_handler(message, gpt_request, version=version)
            except Exception as ex:
                print(repr(ex))
        
        def gpt_request(message, version="gpt-3.5-turbo"):
            try:
                self.bot.send_chat_action(message.chat.id, 'typing')
                request = message.text
                response = self.gpt.generation(request, version)
                if response == False:
                    self.bot.send_message(message.chat.id, f"{self.interface.phrases('You left from GPT', self.lang)}",
                                        reply_markup=self.commands_keyboard(commands, versions))
                    return
                else:
                    self.bot.send_message(message.chat.id, response,
                                        reply_markup=self.commands_keyboard(commands, versions, isgpt=True))
                    
                    self.bot.send_message(message.chat.id, f"{self.interface.phrases('Enter your request', self.lang)}: ",
                                            reply_markup=self.commands_keyboard(commands, versions, isgpt=True))
                    self.bot.register_next_step_handler(message, gpt_request)
            except Exception as ex:
                print(repr(ex))
        
        @self.bot.message_handler(commands=['reg'])
        def register(message):
            try:
                username = message.from_user.id
                self.bot.send_message(message.chat.id, f"{self.interface.phrases('Enter your email', self.lang)}: ",
                                        reply_markup=self.commands_keyboard(commands, versions, isgpt=True))
                self.bot.register_next_step_handler(message, email_input, username=username)
            except Exception as ex:
                print(repr(ex))
        
        def email_input(message, username=None):
            try:
                email = message.text

                if email == "/exit":
                    self.bot.send_message(message.chat.id, f"{self.interface.phrases('You cancelled registration', self.lang)}",
                                          reply_markup=self.commands_keyboard(commands, versions))
                    return
                
                if "@" not in email:
                    self.bot.send_message(message.chat.id, f"{self.interface.phrases('Email must contain @. Enter your email', self.lang)}: ",
                                        reply_markup=self.commands_keyboard(commands, versions, isgpt=True))
                    self.bot.register_next_step_handler(message, email_input, username=username)
                    return
                
                self.bot.send_message(message.chat.id, f"{self.interface.phrases('Enter your password', self.lang)}: ",
                                        reply_markup=self.commands_keyboard(commands, versions, isgpt=True))
                self.bot.register_next_step_handler(message, password_input, username=username, email=email)
            except Exception as ex:
                print(repr(ex))
        
        def password_input(message, username=None, email=None):
            try:
                password = message.text

                if password == "/exit":
                    self.bot.send_message(message.chat.id, f"{self.interface.phrases('You cancelled registration', self.lang)}",
                                          reply_markup=self.commands_keyboard(commands, versions))
                    return

                self.bot.send_message(message.chat.id, f"{self.interface.phrases('You registered successfully', self.lang)}: \n"
                                      f"{self.interface.phrases('Username', self.lang)}: {username}\n"
                                      f"{self.interface.phrases('Email', self.lang)}: {email}\n"
                                      f"{self.interface.phrases('Password', self.lang)}: {password}",
                                        reply_markup=self.commands_keyboard(commands, versions))
            except Exception as ex:
                print(repr(ex))

    def start_polling(self, none_stop: bool = True):
        self.bot.polling(none_stop=none_stop)


def main() -> None:
    tg_bot = TelegramBot("7166707397:AAGVYvapB_wbBc2jcNt44Qb59xaf5JYDiHw")
    tg_bot.start_polling()
