from telebot import TeleBot, types
# from database.dbapi import DatabaseConnector


commands = ["/help", "/reg", "/gpt"]


class TelegramBot:

    def keyboard(self, commands: list) -> types.InlineKeyboardMarkup:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for command in commands:
            markup.add(types.KeyboardButton(command))

        return markup

    def __init__(self, api_token: str) -> None:
        self.bot = TeleBot(api_token)
        self.handlers()
    
    def handlers(self):
        
        @self.bot.message_handler(commands=['start'])
        def start(message) -> None:
            self.bot.send_message(message.chat.id, f"Welcome to the chatgpt_bot, @{message.from_user.username}.\n"
                                            f"The following commands are available:\n\n"
                                            f"/help - show availible commands\n"
                                            f"/reg - register\n"
                                            f"/gpt - run gpt\n\n"
                                            f"@GPT_YandLms_bot", reply_markup=self.keyboard(commands))

        @self.bot.message_handler(commands=['help'])
        def help(message) -> None:
            self.bot.send_message(message.chat.id, f"The following commands are available:\n\n"
                                            f"/help - show availible commands\n"
                                            f"/reg - register\n"
                                            f"/gpt - run gpt\n\n"
                                            f"@GPT_YandLms_bot", reply_markup=self.keyboard(commands))

    def start_polling(self, none_stop: bool = True):
        self.bot.polling(none_stop=none_stop)


def main() -> None:
    tg_bot = TelegramBot("7166707397:AAGVYvapB_wbBc2jcNt44Qb59xaf5JYDiHw")
    tg_bot.start_polling()