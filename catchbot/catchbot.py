import os
from .updater import create_updater
from flask import Flask


class CatchBot(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        bot_token = os.environ['CATCHBOT_TOKEN']
        self.updater = create_updater(bot_token)
        self.updater.start_polling()
