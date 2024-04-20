# ChatGPT bot
![ChatGPT](https://user-images.githubusercontent.com/7910769/227876683-fc4b9c8c-61da-44d0-8f9a-1397e4f4e904.png)

[Bot](https://t.me/GPT_YandLms_bot)

To run this bot you must clone this repository and write to ssh
```shell
git clone https://github.com/MaxBoikov1308/GPTbot.git
cd GPTbot
python -m venv ./venv
cd venv\Scripts
.\activate
```
then open GPTbot and write to ssh
```shell
pip install --upgrade -r .\requirements.txt
```

And enter bot token to
```shell
tg_bot = TelegramBot("")
```


# To-do list 
- [ ] Flask app
  - [ ] Send request to GPT
  - [ ] Get response from GPT
  - [ ] Send response to bot
- [ ] Bot (python)
  - [x] Start
  - [x] Help
  - [ ] Register
    - [ ] Get user data
    - [ ] Send data to db
  - [ ] GPT
    - [ ] Get request from user
    - [ ] Send request to Flask app
    - [ ] Get response from app
    - [ ] Send response to user
- [x] Bot (Telegram)
  - [x] Commands 
  - [x] Bot logo
  - [x] Bot profile
  - [x] Bot start message
- [ ] Database
  - [ ] Create models
  - [ ] Connect to bot and app
