import os
from celery import Celery

from catchbot.router_bot import RouterBot


def _get_broker():
    return 'pyamqp://{user}:{password}@{host}/{vhost}'.format(
        host='rabbitmq:5672',
        user=os.environ['RABBITMQ_DEFAULT_USER'],
        password=os.environ['RABBITMQ_DEFAULT_PASS'],
        vhost=os.environ['RABBITMQ_DEFAULT_VHOST'],
    )


app = Celery('tasks', broker=_get_broker())
bot = RouterBot.from_env()


@app.task
def send_message_to_bot(chat_id, message):
    bot.send_message(chat_id, message)
