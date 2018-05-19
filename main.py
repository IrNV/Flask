from app import app
from users.blueprint import users


app.register_blueprint(users, url_prefix='/users')

if __name__ == '__main__':
    app.run()