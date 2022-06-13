from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Welcome to Cursor!"


@app.route("/hello")
def calendar():
    return "Hello!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
