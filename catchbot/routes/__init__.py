from flask import request, jsonify, redirect

from .message import create_message_list_for_user
from ..catchbot import CatchBot


def _root_post(app):
    if not request.is_json:
        return jsonify(dict(msg='Data must be in json format')), 400

    for chat_id in app.chat_id_list:
        message_list = create_message_list_for_user(request.get_json(cache=False))
        for msg in message_list:
            app.updater.bot.send_message(chat_id, msg)

    return jsonify(dict(msg='Data successfully sent to user'))


def _root_get():
    return redirect('http://t.me/catch_web_hook_bot')


def register_routes(app: CatchBot):
    @app.route('/', methods=['GET', 'POST'])
    def root():
        if request.method == 'POST':
            _root_post(app)
        if request.method == 'GET':
            _root_get()
