import os
import logging
import http.server
import ssl
from flask import Flask


def _get_logger():
    return logging.getLogger(__name__)


def _ssl_wrap_socket(httpd, certfile, keyfile):
    use_ssl = all([
        certfile,
        keyfile,
    ]) and all([
        os.path.exists(certfile),
        os.path.exists(keyfile),
    ])

    if use_ssl:
        httpd.socket = ssl.wrap_socket(
            httpd.socket,
            certfile=certfile,
            keyfile=keyfile,
            server_side=True,
        )
        _get_logger().info('Using https hook server')
    else:
        _get_logger().info('Using http hook server')


class HookServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.flask = Flask()

    def run(self):
        self.flask.run(self.host, self.port)


def create_server(host, port, certfile=None, keyfile=None):
    server = HookServer(host, port)
    return server
