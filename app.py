from flask import Flask, g
from flask.ext.login import LoginManager

import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'la5jsd3m2qa3he@usoi-/lv#as^dfj039endfd'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    """Function to check for user for the LOGIN MANAGER"""
    try:
        return models.Login.get(models.Login.id == userid)
    except models.DoesNotExist:
        return None

@app.before_request
def before_request():
    """connet to the database before each request"""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """close the db connection after each request."""
    g.db.close()
    return response

if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)