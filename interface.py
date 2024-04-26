class Interface:
    def __init__(self):
        pass

    def phrases(self, text: str, lang: str = "🇬🇧English"):
        if text == "Welcome to the chatgpt_bot":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Добро пожаловать в chatgpt_bot"
        if text == "The following commands are available":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Следующие команды доступны"
        if text == "Enter your request":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Введите ваш запрос"
        if text == "Choose correct version":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Выберите правильную версию"
        if text == "You chose":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Вы выбрали"
        if text == "You cancelled registration":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Вы отменили регистрацию"
        if text == "You registered successfully":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Вы успешно зарегистрировались"
        if text == "Enter your email":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Введите ваш email"
        if text == "Enter your password":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Введите ваш пароль"
        if text == "Email must contain one @ and one point. Enter your email":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Email должен содержать @ и точку. Введите ваш email"
        if text == "Enter your username":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Введите ваш юзернейм"
        if text == "You logged in successfully":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Вы успешно вошли в систему"
        if text == "/help - show available commands":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "/help - показать доступные команды"
        if text == "/gpt - run gpt":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "/gpt - запустить gpt"
        if text == "/reg - register":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "/reg - зарегистрироваться"
        if text == "Choose GPT version":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Выберите GPT версию"
        if text == "You left from GPT":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Вы вышли из GPT"
        if text == "Username":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Имя пользователя"
        if text == "Email":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Электронная почта"
        if text == "Password":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Пароль"
        if text == "Something went wrong":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Что-то пошло не так"
        if text == "You are already registered":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Вы уже зарегистрированы"
        if text == "You must register":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Вы должны зарегистрироваться"
        if text == "/delete - delete account":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "/delete - удалить аккаунт"
        if text == "/clear - clear history":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "/clear - очистить историю"
        if text == "Your account has been deleted":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Ваш аккаунт был удален"
        if text == "Your history has been cleared":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Ваша история была очищена"
        if text == "Choose option":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Выберите вариант"
        if text == "You cancelled support":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Вы отменили поддержку"
        if text == "/support - support developers":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "/support - поддержка разработчиков"