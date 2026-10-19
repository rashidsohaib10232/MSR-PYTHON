from flask import Flask

app = Flask(__name__)

@app.route("/users")
def home():
    return "Hello Flask"
@app.route("/user/<id>")
def user(id):
    return f"Hello {id}"
if __name__ == "__main__":
    app.run(debug=True)