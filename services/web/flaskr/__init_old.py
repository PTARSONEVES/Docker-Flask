from flask import (
    Flask, 
    jsonify, 
    send_from_directory, 
    request,
)
#from flask_sqlalcemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os


def create_app():
    app = Flask(__name__)
    media = os.path.abspath(os.path.dirname(__file__))
    media2=media[:len(media)-20]
    arq=f"{media2}\\media"
    md = os.path.isdir(media2)
    print('app-> ',app)
    print('media: ',media2)
    print('basedir: ',md)

    @app.route('/')
    def hello_world():
        return jsonify(hello="world")

    @app.route("/static/<path:filename>")
    def staticfiles(filename):
        return send_from_directory(app.config["STATIC_FOLDER"],filename)

    @app.route("/media/<path:filename>")
    def mediafiles(filename):
        return send_from_directory(app.config["MEDIA_FOLDER"],filename)

    @app.route("/upload", methods=["GET","POST"])
    def upload_file():
        print("testando")
        if request.method=="POST":
            file=request.files["file"]
            filename=secure_filename(file.filename)
            print("testando - POST")
            print('arq: ',arq)
            print('filename: ',filename)
            file.save(arq,filename)
            return """
            <!doctype html>
            <title>upload new File</title>
            <form action="" method=post enctype=multipart/form-data>
                <p><input type=file name=file><input type=submit value=Upload>
            </form>
            """
        if request.method=="GET":
            print("testando - GET")
            return """
            <!doctype html>
            <title>upload new File</title>
            <form action="" method=post enctype=multipart/form-data>
                <p><input type=file name=file><input type=submit value=Upload>
            </form>
            """

    return app