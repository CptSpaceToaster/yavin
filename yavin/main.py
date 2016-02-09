import sqlalchemy
from flask import Flask


app = Flask(__name__)
engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/bye/')
def goodbye():
    return 'Goodbye!'


def main():
    app.run()
