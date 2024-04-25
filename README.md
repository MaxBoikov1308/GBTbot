# ChatGPT bot
![ChatGPT](https://user-images.githubusercontent.com/7910769/227876683-fc4b9c8c-61da-44d0-8f9a-1397e4f4e904.png)

[Bot](https://t.me/GPT_YandLms_bot)

To run this bot you must clone this repository and write to ssh
```shell
git clone https://github.com/MaxBoikov1308/GPTbot.git
cd GPTbot
python -m venv ./venv
```
then open GPTbot and write to ssh
```shell
pip install --upgrade -r .\requirements.txt
```

And enter bot token to
```python
tg_bot = TelegramBot("...")
```


# To-do list 
- [x] App
  - [X] Send request to GPT
  - [x] Get response from GPT
  - [x] Send response to bot
- [ ] Bot (python)
  - [x] Start
  - [x] Help
  - [ ] Register
  - [x] GPT
    - [x] Get request from user
    - [x] Send request to app
    - [x] Get response from app
    - [x] Send response to user
- [x] Bot (Telegram)
  - [x] Commands 
  - [x] Bot logo
  - [x] Bot profile
  - [x] Bot start message
- [ ] Database
  - [x] Create models
  - [ ] Connect to bot and app
