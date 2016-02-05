import sqlalchemy
from flask import Flask


app = Flask(__name__)
engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)


@app.route('/')
def hello_world():
    return 'Hello World!'


def main():
    app.run()


if __name__ == '__main__':
    main()
