#Веб-сервере на питоне
from flask import Flask

main = Flask(__name__)

@main.route('/')
def index():
    return '<html>\n<body>\n<h1>Всем привет, я только проснулся</h1>\n<head>\n<h2>Da</h2>\n</head>\n</body>\n</html>'

@main.route('/Geppa')
def Geppa():
    return '<html>\n<body>\n<h1>Добро пожаловать в Жеппу</h1>\n<h6>Снова...</h6>\n</body></html>'
if __name__ == "__main__":
    main.run(debug=True)
