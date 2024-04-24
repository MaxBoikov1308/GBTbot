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
        if text == "Email must contain @. Enter your email":
            if lang == "🇬🇧English":
                return text
            elif lang == "🇷🇺Русский":
                return "Email должен содержать @. Введите ваш email"
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