import os
from .updater import create_updater
from flask import Flask


class CatchBot(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        bot_token = os.environ['CATCHBOT_TOKEN']
        self.updater = create_updater(bot_token)

    def run(self, host=None, port=None, debug=None, **options):
        self.tg_updater.start_polling()
        if not host:
            host = os.environ['CATCHBOT_HOST']
            port = int(os.environ['CATCHBOT_PORT'])
            debug = int(os.environ['CATCHBOT_DEBUG'])
        super().run(host, port, debug)
