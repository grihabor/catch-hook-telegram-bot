from catchbot.hook_server import create_server
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

