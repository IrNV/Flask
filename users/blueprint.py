from flask import Blueprint
from flask import render_template
from models import User
from app import db

users = Blueprint('users', __name__, template_folder='templates', static_folder='static')


@users.route("/")
def users_page():
    # users = ["Admin", "User1", "User2"]
    all_users = User.query.all()
    return render_template("users/index.html", users=all_users)


@users.route('/click/<data>')
def user_click(data):
    print(data)
    user = User.query.filter(User.username == data).first()
    print("User on clicked:", user)
    user.click_count += 1
    db.session.commit()
    all_users = User.query.all()
    return render_template("users/index.html", users=all_users)