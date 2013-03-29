from flask import Flask, render_template
from listlog import app, db
from models import Item

@app.route('/')
def index():
    return render_template("index.html", items = Item.objects())
