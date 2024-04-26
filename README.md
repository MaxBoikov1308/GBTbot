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
- [x] Bot
  - [x] Start
  - [x] Language selection
    - [x] English
    - [x] Russian
  - [x] Delete account
  - [x] Help
  - [x] Register
  - [x] GPT
    - [X] Send request to GPT
    - [x] Get response from GPT
    - [x] Send response to user
      - [x] Formating
      - [ ] Stream ?
- [x] Database
  - [x] Models
    - [x] Users
    - [x] Requests
  - [x] SQLAlchemy initialisation
- [x] initialisation
  - [x] Threading