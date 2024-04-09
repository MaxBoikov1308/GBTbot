# ChatGPT bot

[Bot id](https://t.me/GPT_YandLms_bot)

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
then run run.py
```shell
python run.py
```

# To-do list 
- [ ] GPT-parser
  - [ ] Send request 
  - [ ] Get response from GPT
  - [ ] Requests history ?
- [ ] Bot core (python)
  - [x] Buttons
  - [ ] DB connection 
  - [ ] GPT connection
- [x] Bot (Telegram)
  - [x] Profile
  - [x] Start message
  - [x] Buttons
- [ ] Server?
- [ ] DB
  - [ ] Activate orm (sqlalchemy)
    - [ ] User Telegram ID
    - [ ] Requests history ?
    - [ ] Premium subscription ?