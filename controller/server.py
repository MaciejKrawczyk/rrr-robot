from flask import Flask

from controller.server_endpoints import setup_routes


def create_app(queue):
    app = Flask(__name__)
    setup_routes(app, queue)
    return app


def run_server(queue, host='0.0.0.0', port=5000):
    app = create_app(queue)
    app.run(host=host, port=port)
