import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()
PORT = os.getenv("PORT")

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


def run():
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)

if __name__ == "__main__":
    run()
