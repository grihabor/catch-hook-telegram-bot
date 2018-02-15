import os
from .updater import create_updater


class RouterBot:
    def __init__(self, token, chat_id_list):
        self.updater = create_updater(token)
        self.chat_id_list = chat_id_list

    @classmethod
    def from_env(cls):
        bot_token = os.environ['CATCHBOT_TOKEN']
        chat_id_list = os.environ['CATCHBOT_CHATS'].split(',')
        return RouterBot(bot_token, chat_id_list)

    def start(self):
        self.updater.start_polling()
