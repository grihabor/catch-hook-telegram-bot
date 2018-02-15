import os
from .updater import create_updater


class RouterBot:
    def __init__(self, token):
        self.updater = create_updater(token)

    @classmethod
    def from_env(cls):
        bot_token = os.environ['CATCHBOT_TOKEN']
        return RouterBot(bot_token)

    def start(self):
        self.updater.start_polling()

    def send_message(self, chat_id, text):
        self.updater.bot.send_message(chat_id=chat_id, text=text)
