#Веб-сервере на питоне
from flask import Flask, render_template, url_for

main = Flask(__name__)


@main.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    main.run(host='0.0.0.0', port=8080, debug=True)
