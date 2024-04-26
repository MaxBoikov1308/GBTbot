from threading import Thread
from telegram import main


class TelegramThread(Thread):
    def run(self) -> None:
        main()

if __name__ == '__main__':
    main()
