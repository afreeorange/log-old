TITLE= "Log"
AUTHOR="Nikhil Anand"
DEBUG = True
MONGODB_SETTINGS = {'DB': "log", 'PORT': 27017}
SECRET_KEY = "MOobPQgBMHkIuanurC+NjVq08M+U9f7o"
POST_TYPES = [('video', 'Video'), 
              ('music', 'Music'), 
              ('article', 'Article'), 
              ('picture', 'Picture'), 
              ('quote', 'Quote'), 
              ('chat', 'Chat'), 
              ('misc', 'Misc')]
INFINITE_SCROLL = False
ITEMS_PER_PAGE = 5
ITEMS_IN_NEWSFEED = 15
USERS = {
    'admin': {
        'password': 'pass',
        'name': 'Nikhil'
    },
    'anotheradmin': {
        'password': 'pass2',
        'name': 'Rufus'
    }
}
COPYRIGHT_MESSAGE = """
<p>
  <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/deed.en_US">
    This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/deed.en_US">Creative Commons Attribution-NonCommercial 3.0 Unported License
  </a>.
</p>
"""
ERROR_MESSAGES = {
    "404": """
            <h1>I'm sorry, Dave</h1>
            <br />
            <h2>I couldn't find that :(</h2>
           """,
    "500": """
            <h1>Whoops&hellip;</h1>
            <br />
            <h2>It's not you, it's me</h2>
           """
}
