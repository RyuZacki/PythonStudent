"""       ---------------------- FLASK ----------------------       """

# Простое WSGI-приложение

from flask import Flask # <-- Импорт фласка

app = Flask(__name__) # <-- Создаём экземпляр класса Flask, первым аргументом должны указать имя нашего приложения


@app.route("/") # <-- Указываем URL адрес, по которому будет отрабатывать отработчик
@app.route("/index")
def index(): # <-- Обработчик index
    return "index"


@app.route("/about")
def about(): # <-- Ещё один бработчик
    return "<h1>О сайте</h1>"


if __name__ == "__main__":
    app.run(debug=True) # <-- Запуск локального веб-сервера, debug=True позволяет видеть все ошибки в браузере