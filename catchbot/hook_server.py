import BaseHTTPServer, SimpleHTTPServer
import ssl


def _get_logger():
    return logging.getLogger(__name__)
    

def create_server(host, port, *, certfile=None, keyfile=None):
    use_ssl = all([
        certfile,
        keyfile,
    ]) and all([
        os.path.exists(certfile),
        os.path.exists(keyfile),
    ])
    
    httpd = BaseHTTPServer.HTTPServer((host, port), SimpleHTTPServer.SimpleHTTPRequestHandler)
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
   
    return httpd
