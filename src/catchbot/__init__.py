from .routes import register_routes
from flask import Flask
from .router_bot import RouterBot

__version__ = '0.0.2'

app = Flask(__name__)
register_routes(app)
