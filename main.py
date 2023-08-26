from flask import Flask

app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<p>Hello, World!<p>" 


@app.route("/consol")
def hello_world2():
    return '<h1>если ты играешь через консоль то ты консольщик </h1>'

@app.route("/kompukter")
def hello_world3():
    return '<h1>если ты играешь через компьютер то ты пкашер</h1>'



@app.route("/telefon")
def hello_world4():
    return '<h1>если ты играешь в телефон то ты телефонист</h1>'



app.run(debug=True)
