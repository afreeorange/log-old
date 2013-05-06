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

# http://docs.mongodb.org/manual/core/indexes/#multikey-indexes
class Item(Document):
    title = StringField(required=False, max_length=255)
    content = StringField(required=True)
    posted = DateTimeField(required=True, default=datetime.now())
    updated = DateTimeField(required=True, default=datetime.now())
    post_type = StringField(required=True, choices=post_types,
                              default='misc')
    tags = ListField(StringField(max_length=30))
    meta = {
        'indexes': ['-posted', 'title', 'tags'],
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
    posted = wtforms.DateTimeField('Posted', default=datetime.now())


class LoginForm(Form):
    username = wtforms.TextField('Username', [wtforms.validators.Required()])
    password = wtforms.PasswordField('Password', [wtforms.validators.Required()])
    remember = wtforms.BooleanField('Forget you not?', default=False)

# http://pythonhosted.org/Flask-Login/#your-user-class
# Can inherit the 'UserMixin' class as well...
class User():
    def __init__(self, id):
        self.id = id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

class input_filter():
    def __init__(self, arg):
        self.arg = arg
