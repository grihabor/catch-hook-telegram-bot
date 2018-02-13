import json

import itertools
from flask import request, jsonify
from ..catchbot import CatchBot


def construct_message_for_user(json_obj):
    return json.dumps(json_obj, indent=2)


def construct_message_list_for_user(json_obj, step=32):
    msg = construct_message_for_user(json_obj)
    lines = msg.split('\n')

    return [
        itertools.islice(lines, i, i + step)
        for i
        in range(0, len(lines), step)
    ]


def register_routes(app: CatchBot):
    @app.route('/', methods=['GET', 'POST'])
    def root():
        if request.method == 'POST':
            if not request.is_json:
                return jsonify(dict(msg='Data must be in json format')), 400

            for chat_id in app.chat_id_list:
                message_list = construct_message_list_for_user(request.get_json(cache=False))
                for msg in message_list:
                    app.updater.bot.send_message(chat_id, msg)

            return jsonify(dict(msg='Data successfully sent to user'))

        return jsonify(dict(msg='Catch hook telegram bot'))
