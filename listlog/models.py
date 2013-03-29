from datetime import datetime
from mongoengine import Document, StringField, DateTimeField

class Item(Document):
    title = StringField(required = False)
    content = StringField(required = True)
    posted = DateTimeField(required = True, default = datetime.now())
    meta = {
        'indexes': ['-posted', 'title'],
        'ordering': ['-posted']
    }
