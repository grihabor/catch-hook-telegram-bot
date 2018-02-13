import json

from flask import request, jsonify
from ..catchbot import CatchBot


def construct_message_for_user(json_obj):
    return '```' + json.dumps(json_obj, indent=2) + '```'


def register_routes(app: CatchBot):
    @app.route('/', methods=['GET', 'POST'])
    def root():
        if request.method == 'POST':
            if not request.is_json:
                return jsonify(dict(msg='Data must be in json format')), 400

            for chat_id in app.chat_id_list:
                app.updater.bot.send_message(
                    chat_id,
                    construct_message_for_user(request.get_json(cache=False))
                )

            return jsonify(dict(msg='Data successfully sent to user'))

        return jsonify(dict(msg='Catch hook telegram bot'))
