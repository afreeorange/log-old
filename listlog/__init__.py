from datetime import datetime

from flask import Flask
from jinja2 import Environment
from flask.ext.mongoengine import MongoEngine
from flaskext.markdown import Markdown
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('settings')
app.config['CSRF_ENABLED'] = True
app.config['CURRENT_YEAR'] = datetime.now().strftime("%Y")

db = MongoEngine(app)
markdown = Markdown(app)
login_manager = LoginManager()
login_manager.setup_app(app)

from listlog import views, models, helpers, login

if __name__ == '__main__':
    app.run()
