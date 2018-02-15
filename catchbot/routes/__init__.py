import os
from flask import request, jsonify, redirect

from .message import create_message_for_user
from ..tasks import send_message_to_bot


def _get_info_from_headers(headers):
    try:
        return {'_event': headers['X-GitHub-Event']}
    except KeyError:
        pass

    return {}


def _hook(chat_id, hash):
    if not request.is_json:
        return 'Data must be in json format', 400

    json_obj = request.get_json(cache=False)
    json_obj.update(_get_info_from_headers(request.headers))
    msg = create_message_for_user(json_obj)

    chat_id = os.environ['CATCHBOT_CHAT_ID_LIST']

    send_message_to_bot.delay(chat_id, msg)

    return 'OK', 200


def _root():
    return redirect('http://t.me/catch_web_hook_bot', code=302)


def register_routes(app):
    @app.route('/hooks/<chat_id>/<hash>', methods=['POST'])
    def hook(chat_id, hash):
        return _hook(chat_id, hash)

    @app.route('/', methods=['GET'])
    def root():
        return _root()




