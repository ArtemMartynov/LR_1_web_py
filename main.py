#Веб-сервере на питоне
from flask import Flask, render_template, url_for, abort
from os.path import exists

main = Flask(__name__)


@main.route('/')
def index():
    return render_template("index.html")


@main.route('/<string:name>')
def intresting(name):
    if exists("./templates/"+name) == True:
        return render_template(name)
    else:
        return abort(404)


if __name__ == "__main__":
    main.run(host='0.0.0.0', port=8080, debug=True)

