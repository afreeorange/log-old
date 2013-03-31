from datetime import datetime
from mongoengine import Document, StringField, DateTimeField

class Item(Document):
    from listlog import app
    title = StringField(required = False)
    content = StringField(required = True)
    posted = DateTimeField(required = True, default = datetime.now())
    filed_under = StringField(required = True, choices = app.config['POST_TYPES'], default = 'misc')
    meta = {
        'indexes': ['-posted', 'title'],
        'ordering': ['-posted']
    }
