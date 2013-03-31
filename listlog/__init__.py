from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('settings')

db = MongoEngine(app)

from listlog import views
from listlog import models

if __name__ == '__main__':
    app.run()
