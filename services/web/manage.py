from flask.cli import FlaskGroup
from project import create_app

cli = create_app()
print(__name__)
print(teste)
if __name__=="__main__":
    cli()