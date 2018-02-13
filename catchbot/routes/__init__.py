import json

from flask import request, jsonify
from ..catchbot import CatchBot


def register_routes(app: CatchBot):
    @app.route('/', methods=['GET', 'POST'])
    def root():
        if request.method == 'POST':
            if not request.is_json:
                return jsonify(dict(msg='Data must be in json format')), 400
            app.updater.send_message(
                205613939,
                json.dumps(request.get_json(cache=False)),
            )
            return jsonify(dict(msg='Data successfully sent to user'))

        return jsonify(dict(msg='Catch hook telegram bot'))
