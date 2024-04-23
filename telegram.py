from telebot import TeleBot, types
# from database.dbapi import DatabaseConnector
from app import GPT


commands = ["/help", "/reg", "/gpt"]
versions = ["gpt-3.5-turbo", "gpt-4"]


class TelegramBot:

    def commands_keyboard(self, commands: list, versions: list, ischoose: bool = False, isgpt: bool = False, isreg: bool = False) -> types.InlineKeyboardMarkup:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        if ischoose:
            for version in versions:
                markup.add(types.KeyboardButton(version))
        elif isgpt:
            markup.add(types.KeyboardButton('/exit'))
        else:
            for command in commands:
                markup.add(types.KeyboardButton(command))

        return markup

    def __init__(self, api_token: str) -> None:
        self.bot = TeleBot(api_token)
        self.handlers()
        self.gpt = GPT()
    
    def handlers(self):
        
        @self.bot.message_handler(commands=['start'])
        def start(message) -> None:
            self.bot.send_message(message.chat.id, f"Welcome to the chatgpt_bot, @{message.from_user.username}.\n"
                                            f"The following commands are available:\n\n"
                                            f"/help - show availible commands\n"
                                            f"/gpt - run gpt\n\n"
                                            f"@GPT_YandLms_bot", reply_markup=self.commands_keyboard(commands, versions))

        @self.bot.message_handler(commands=['help'])
        def help_message(message) -> None:
            self.bot.send_message(message.chat.id, f"The following commands are available:\n\n"
                                            f"/help - show availible commands\n"
                                            f"/gpt - run gpt\n\n"
                                            f"@GPT_YandLms_bot", reply_markup=self.commands_keyboard(commands, versions))
        
        @self.bot.message_handler(commands=['gpt'])
        def gpt(message) -> None:
            self.bot.send_message(message.chat.id, f"Hello, @{message.from_user.username}, choose GPT version:\n",
                                  reply_markup=self.commands_keyboard(commands, versions, True))
            self.bot.register_next_step_handler(message, choose_version)
        
        def choose_version(message):
            try:
                version = message.text
                if version not in versions:
                    self.bot.send_message(message.chat.id, "Choose correct version",
                                        reply_markup=self.commands_keyboard(commands, versions, True))
                    self.bot.register_next_step_handler(message, choose_version)
                    return
                self.bot.reply_to(message, "you choose: " + version,
                                    reply_markup=self.commands_keyboard(commands, versions))
                self.bot.send_message(message.chat.id, "Enter your request: ",
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
                    self.bot.send_message(message.chat.id, "You left from GPT",
                                        reply_markup=self.commands_keyboard(commands, versions))
                    return
                else:
                    self.bot.send_message(message.chat.id, response,
                                        reply_markup=self.commands_keyboard(commands, versions, isgpt=True))
                    
                    self.bot.send_message(message.chat.id, "Enter your request: ",
                                            reply_markup=self.commands_keyboard(commands, versions, isgpt=True))
                    self.bot.register_next_step_handler(message, gpt_request)
            except Exception as ex:
                print(repr(ex))
        
        @self.bot.message_handler(commands=['reg'])
        def register(message):
            try:
                username = message.from_user.id
                self.bot.send_message(message.chat.id, "Enter your email: ",
                                        reply_markup=self.commands_keyboard(commands, versions, isgpt=True))
                self.bot.register_next_step_handler(message, email_input, username=username)
            except Exception as ex:
                print(repr(ex))
        
        def email_input(message, username=None):
            try:
                email = message.text

                if email == "/exit":
                    self.bot.send_message(message.chat.id, "You cancelled registration",
                                          reply_markup=self.commands_keyboard(commands, versions))
                    return
                
                if "@" not in email:
                    self.bot.send_message(message.chat.id, "Email must contain @. Enter your email: ",
                                        reply_markup=self.commands_keyboard(commands, versions, isgpt=True))
                    self.bot.register_next_step_handler(message, email_input, username=username)
                    return
                
                self.bot.send_message(message.chat.id, "Enter your password: ",
                                        reply_markup=self.commands_keyboard(commands, versions, isgpt=True))
                self.bot.register_next_step_handler(message, password_input, username=username, email=email)
            except Exception as ex:
                print(repr(ex))
        
        def password_input(message, username=None, email=None):
            try:
                password = message.text

                if password == "/exit":
                    self.bot.send_message(message.chat.id, "You cancelled registration",
                                          reply_markup=self.commands_keyboard(commands, versions))
                    return

                self.bot.send_message(message.chat.id, f"You registered successfully\n"
                                      f"Username: {username}\n"
                                      f"Email: {email}\n"
                                      f"Password: {password}",
                                        reply_markup=self.commands_keyboard(commands, versions))
            except Exception as ex:
                print(repr(ex))

    def start_polling(self, none_stop: bool = True):
        self.bot.polling(none_stop=none_stop)


def main() -> None:
    tg_bot = TelegramBot("7166707397:AAGVYvapB_wbBc2jcNt44Qb59xaf5JYDiHw")
    tg_bot.start_polling()
