from flask.cli import FlaskGroup
from project import app
#from project import create_app

#cli = create_app()
#print(__name__)
#print(teste)
#FLASK_APP=project/__init__.py
#FLASK_RUN_PORT=5001

cli=FlaskGroup(app)

if __name__=="__main__":
    cli()
#    app=create_app()
#    cli()
