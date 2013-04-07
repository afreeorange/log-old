DEBUG = True
MONGODB_SETTINGS = {'DB': "listlog"}
SECRET_KEY = "MOobPQgBMHkIuanurC+NjVq08M+U9f7o"
POST_TYPES = [('video', 'Video'), 
              ('music', 'Music'), 
              ('article', 'Article'), 
              ('picture', 'Picture'), 
              ('quote', 'Quote'), 
              ('chat', 'Chat'), 
              ('misc', 'Misc')]
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
