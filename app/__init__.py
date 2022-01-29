from flask import Flask
from app.routes import space_routes
# from app.services import scheduler_daily
import atexit

# from apscheduler.


def create_app():
    app = Flask(__name__)

    app.config["JSON_SORT_KEYS"] = False

    space_routes.init_app(app)
   

    return app