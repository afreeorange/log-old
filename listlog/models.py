from datetime import datetime

from listlog import app
from mongoengine import Document, StringField, DateTimeField
from flask.ext.mongoengine.wtf import model_form

post_types = app.config['POST_TYPES']


class Item(Document):
    title = StringField(required=False)
    content = StringField(required=True)
    posted = DateTimeField(required=True, default=datetime.now())
    filed_under = StringField(required=True, choices=post_types,
                              default='misc')
    meta = {
        'indexes': ['-posted', 'title'],
        'ordering': ['-posted']
    }

ItemForm = model_form(Item)
