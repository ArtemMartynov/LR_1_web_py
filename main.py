#Веб-сервере на питоне
from flask import Flask

main = Flask(__name__)


@main.route('/')
@main.route('/home')
def index():
    return '<html>\n<body>\n<h1>Всем привет, я только проснулся</h1>\n<head>\n<h2>Da</h2>\n</head>\n</body>\n</html>'


@main.route('/user/<string:name>/<int:id>')
def user(name,id):
    return 'User Name: '+ name + '\nid:' + str(id)

@main.route('/Geppa')
def Geppa():
    return '<html>\n<body>\n<h1>Добро пожаловать в Жеппу</h1>\n<h6>Снова...</h6>\n</body></html>'


if __name__ == "__main__":
    main.run(host = '127.0.0.1', port = 8080, debug=True)
