#Веб-сервере на питоне
from flask import Flask, render_template, url_for

main = Flask(__name__)


@main.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
<<<<<<< HEAD
    main.run(host='0.0.0.0', port=8080, debug=True)
=======
    main.run(host = '127.0.0.1', port = 8080, debug=True)
>>>>>>> 36033fad04b273e173c8910719f99e84b2d40559
