TITLE= "listlog"
AUTHOR="Nikhil Anand"
DEBUG = True
MONGODB_SETTINGS = {'DB': "listlog", 'PORT': 27017}
SECRET_KEY = "MOobPQgBMHkIuanurC+NjVq08M+U9f7o"
POST_TYPES = [('video', 'Video'), 
              ('music', 'Music'), 
              ('article', 'Article'), 
              ('picture', 'Picture'), 
              ('quote', 'Quote'), 
              ('chat', 'Chat'), 
              ('misc', 'Misc')]
INFINITE_SCROLL = True
ITEMS_PER_PAGE = 5
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
ITEMS_IN_NEWSFEED = 15
