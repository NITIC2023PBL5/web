import os
from dotenv import load_dotenv
from flask import Flask

from src.routes.api import api_app
from src.routes.notify import notify_app

load_dotenv()
PORT = os.getenv("PORT")

app = Flask(__name__)
app.register_blueprint(api_app, url_prefix="/api")
app.register_blueprint(notify_app, url_prefix="/notify")


@app.route("/")
def hello_world():
    return "Hello, World!"


def run():
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)


if __name__ == "__main__":
    run()
