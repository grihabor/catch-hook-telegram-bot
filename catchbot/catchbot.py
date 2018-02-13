import os
from .hook_server import create_server
from .updater import create_updater


class CatchBot:
    def __init__(self, 
                 token,
                 host,
                 port,
                 certfile,
                 keyfile,):

        self.updater = create_updater(token)
        self.httpd = create_server(
            host,
            port,
            certfile,
            keyfile,
        )
                 
    def start(self):
        self.updater.start_polling()
        self.httpd.serve_forever()

    def stop(self):
        self.updater.stop()

    @classmethod
    def from_env(cls):
        token = os.environ['CATCHBOT_TOKEN']

        host = os.environ['CATCHBOT_HOST']
        port = int(os.environ['CATCHBOT_PORT'])

        cert = os.getenv('CATCHBOT_CERT', None)
        key = os.getenv('CATCHBOT_KEY', None)

        return CatchBot(token=token,
                        host=host,
                        port=port,
                        certfile=cert,
                        keyfile=key,)


