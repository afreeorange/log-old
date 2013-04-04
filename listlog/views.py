import os
from math import ceil

from flask import Flask, render_template, send_from_directory, flash, request, redirect
from listlog import app, db
from models import Item, ItemForm
from helpers import *

items_per_page = app.config['ITEMS_PER_PAGE']


@app.route('/post', methods=['GET', 'POST'])
def form_post():
    """ Show the form to post items. Perhaps the only form on the site...
    """
    form = ItemForm(request.form)
    if request.method == 'POST':
        #form.save()
        flash('Saved item')
        return redirect("/")
    return render_template("forms/post.html", form=form)


@app.route('/page/<page_number>')
@app.route('/page')
@app.route('/')
@app.route('/index')
def index(page_number=1):
    """ Display a paginated home page of items, ordered by posting date.
        Implement this when you understand it fully:
        http://flask.pocoo.org/snippets/44/
    """
    # Clean up the page number. I found out that Python's 'pass-by-object'
    # when writing this simple method and my head's a little... shaken.
    page_number = enforce_integer(page_number)

    # Quick calculations for pagination
    number_of_items = Item.objects().count()
    number_of_pages = int(ceil(number_of_items / float(items_per_page)))
    start = (page_number - 1) * items_per_page
    end = start + items_per_page

    # Use array splicing (docs-recommended over start() and limit())
    # to paginate results
    return render_template("index.html",
                           items=Item.objects[start:end].order_by('-posted'), **locals())


@app.route('/favicon.ico')
def favicon():
    """ Send the favicon. Static, so should be handled by server in production.
    """
    return send_from_directory(os.path.join(app.root_path, 'static/img'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')
