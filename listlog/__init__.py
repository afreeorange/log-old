from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "listlog"}
app.config["SECRET_KEY"] = "1BF1802D-B99B-4470-8F08-305A4A72E24D"
db = MongoEngine(app)

from listlog import views
from listlog import models

if __name__ == '__main__':
    app.run()
