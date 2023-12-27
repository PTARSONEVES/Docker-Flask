from flask.cli import FlaskGroup
from flaskr import create_app

cli = create_app()

cli=FlaskGroup(app)

if __name__=="__main__":
    cli()
