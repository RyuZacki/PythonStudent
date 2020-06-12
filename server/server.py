from datetime import datetime

from flask import Flask

app = Flask(__name__)
server_start = datetime.now().strftime('%H:%M:%S %d/%m/%Y')

@app.route("/")
def hello():
    return 'Hello, User! <a href="/status">статус</a>'

@app.route("/status")
def status():
    return {
        'status' : 'OK',
        'name' : 'Skillbox Messenger',
        'server_start_time' : server_start,
        'server_current_time' : datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    }

app.run()
