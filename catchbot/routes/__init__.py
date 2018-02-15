import itertools
from flask import request, jsonify, redirect

from .message import create_message_for_user
from ..catchbot import CatchBot


def _get_info_from_headers(headers):
    try:
        return {'_event': headers['X-GitHub-Event']}
    except KeyError:
        pass

    return {}


def send_message_to_bot(message_list):
    pass


def _root_post(app):
    if not request.is_json:
        return 'Data must be in json format', 400

    json_obj = request.get_json(cache=False)
    json_obj.update(_get_info_from_headers(request.headers))
    message_list = create_message_for_user(json_obj)

    send_message_to_bot(message_list)
    for msg in message_list:
        app.updater.bot.send_message(chat_id, msg)

    return 'OK', 200


def _root_get():
    return redirect('http://t.me/catch_web_hook_bot', code=302)


def register_routes(app: CatchBot):
    @app.route('/', methods=['GET', 'POST'])
    def root():
        if request.method == 'POST':
            return _root_post(app)
        if request.method == 'GET':
            return _root_get()

        return 'Method not allowed', 405




