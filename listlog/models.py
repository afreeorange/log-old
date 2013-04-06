from datetime import datetime

from listlog import app
from mongoengine import Document, StringField, DateTimeField, ListField
from flask.ext.mongoengine.wtf import model_form


# http://flask.pocoo.org/snippets/60/
#from flask.ext.wtf import Form
#from wtforms.ext.appengine.db import model_form

from flask.ext.wtf import Form
import wtforms

post_types = app.config['POST_TYPES']


class Item(Document):
    title = StringField(required=False, max_length=255)
    content = StringField(required=True)
    posted = DateTimeField(required=True, default=datetime.now())
    post_type = StringField(required=True, choices=post_types,
                              default='misc')
    tags = ListField(StringField(max_length=30))
    meta = {
        'indexes': ['-posted', 'title'],
        'ordering': ['-posted']
    }

    # 'Magic method' to tell class how to print itself. Nice for debugging!
    # Sublime difference between __str__ and __repr__
    # http://satyajit.ranjeev.in/2012/03/14/python-repr-str.html
    def __str__(self):
        return '%s - (%s) (Titled "%s") - %s...' % (self.posted, self.post_type, self.title, self.content[:30])


# Create a form object out of the MongoEngine class definition. Very convenient.
ItemForm = model_form(Item)


class NewItemForm(Form):
    title = wtforms.TextField('Item Title', [wtforms.validators.length(max=255)])
    content = wtforms.TextAreaField('Content', [wtforms.validators.Required()])
    post_type = wtforms.RadioField('Type', choices=post_types, default="misc") 
