import flask

from bp_api.views import bp_api
from bp_posts.views import bp_posts

import config_logger


def create_and_config_app(config_path):

    app = flask.Flask(__name__)

    app.register_blueprint(bp_posts)
    app.register_blueprint(bp_api, url_prefix='/api')

    app.config.from_pyfile(config_path)
    config_logger.config(app)

    return app

app = create_and_config_app("config.py")

@app.errorhandler(404)
def page_error_404(error):
    return "Такой страницы нет", 404

@app.errorhandler(500)
def page_error_500(error):
    return f"На сервере произошла ошибка {error}", 500


if __name__ == '__main__':
    app.run(host='127.8.8.1', port=8000, debug=True)
