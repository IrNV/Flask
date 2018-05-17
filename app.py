from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/user")
def user_page():
    user = "Admin"
    return render_template("user.html", name=user)


@app.route("/about")
def about_page():
    return "Page about"

app.run(debug=True)
