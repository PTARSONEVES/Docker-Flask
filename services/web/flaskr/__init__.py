from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)
    print('app-> ',app)

    @app.route('/')
    def hello_world():
        return jsonify(hello="world")

    return app