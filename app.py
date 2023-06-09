import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()
PORT = os.getenv("PORT")

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(port=PORT)
