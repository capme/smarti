import logging
from werkzeug.contrib.cache import RedisCache
from flask import Flask

from config import config

LOGGING_LEVEL = {
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
    'WARNING': logging.WARNING,
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR
}


def handle_error(app, error):
    pass


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .api import api_bp as api_blueprint

    app.register_blueprint(api_blueprint)

    app.cache = RedisCache(host=app.config['REDIS_HOST'],
                           db=7)

    if app.debug is False and app.testing is False:
        logging_initialize(app)
    else:
        log_formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
        app.logger.handlers[0].setFormatter(log_formatter)
        app.logger.setLevel(logging.DEBUG)

    """Unhandled exception"""
    @app.errorhandler(Exception)
    def handle_exception(error):
        return handle_error(app, error)

    return app


def logging_initialize(app):
    pass
