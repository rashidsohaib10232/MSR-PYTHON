from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask"

@app.route("/user/<int:id>")    # fir accecpting only integer <int:id>
def user(id):
    return f"User ID {id}"

@app.route("/price/<float:amount>")
def price(amount):
    return f"Amount {amount}"

@app.route("/Name/<string:name>")
def uname(name):
    return f'Your name is {name}'
if __name__ == "__main__":
    app.run(debug=True)