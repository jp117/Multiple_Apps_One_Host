from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "you're the best rubber ducky"


if __name__ == "__main__":
    app.run()
