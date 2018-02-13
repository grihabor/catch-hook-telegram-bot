import os
import logging
import http.server
import ssl


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


def create_server(host, port, certfile=None, keyfile=None):
    httpd = http.server.HTTPServer(
        (host, port),
        http.server.SimpleHTTPRequestHandler,
    )
    _ssl_wrap_socket(httpd, certfile, keyfile)
    return httpd
