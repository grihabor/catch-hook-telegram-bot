from catchbot.router_bot import RouterBot
from .celery_app import app


bot = RouterBot.from_env()


@app.task
def send_message_to_bot(chat_id, message):
    bot.send_message(chat_id, message)
