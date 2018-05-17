from flask import Flask
app = Flask(__name__)


@app.route("/")
def main_page():
    return "Hello World!"


@app.route("/user")
def user_page():
    return "Hello user!"


@app.route("/about")
def about_page():
    return "Page about"

app.run(debug=True)
