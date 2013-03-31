import os
from flask import Flask, render_template, send_from_directory, flash
from listlog import app, db
from models import Item
from helpers import *
items_per_page = app.config['ITEMS_PER_PAGE']


@app.route('/post')
def form_post():
    return render_template("index.html")


""" Display a paginated home page of items, ordered by posting date.
"""
@app.route('/page/<page_number>')
@app.route('/')
@app.route('/index')
def index(page_number = 1):
    # Quick calculations for pagination
    start = (int(page_number) - 1) * items_per_page
    stop = start + items_per_page

    # Array splicing is recommended over skip() and limit() to paginate results
    return render_template("index.html", items = Item.objects[start:stop].order_by('-posted'))


""" Send the favicon. Should be handled by server in production.
"""
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
