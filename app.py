from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/users")
def users_page():
    users = ["Admin", "User1", "User2"]
    return render_template("users.html", users=users)


@app.route("/about")
def about_page():
    return "Page about"

app.run(debug=True)
