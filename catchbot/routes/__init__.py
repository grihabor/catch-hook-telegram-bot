import json

import itertools
from flask import request, jsonify
from ..catchbot import CatchBot

_structure = {
    'repository': 'repository.name',
    'event': '',
}

def filter_important_data_for_user(json_obj):
    repo = json_obj['repository']
    
    return '\n'.join([
        'Name',
        '----',
        repo['name'],
    ])



def construct_message_list_for_user(json_obj, step=32):
    json_obj = filter_important_data_for_user(json_obj)
    lines = msg.split('\n')

    return [
        '```' + '\n'.join(list(itertools.islice(lines, i, i + step))) + '```'
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
