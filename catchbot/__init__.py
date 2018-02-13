from .catchbot import CatchBot
from .routes import register_routes

__version__ = '0.0.1'

app = CatchBot(__name__)
register_routes(app)
