from flask import Flask # Вытащил объект


app = Flask(__name__)


@app.route('/<x>/<y>') # Создание главной страницы (адрес)
def main(x, y):
    return str(int(x) + int(y))




app.run(port=8080)
