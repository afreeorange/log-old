from flask import render_template, request, flash, redirect, url_for
from listlog import app, login_manager
from models import LoginForm, User
from flask.ext.login import login_user, logout_user, login_required, current_user

# Achieved using these:
# http://pythonhosted.org/Flask-Login/#how-it-works
# and then: 
# http://stackoverflow.com/a/12081788

valid_users = app.config['USERS']


@login_manager.user_loader
def load_user(userid):
	""" Return the user object. This is a valid user at this point...
	"""
	return User(id=userid)


@app.route("/login", methods=['GET', 'POST'])
def login():
	""" Log in a valid user.
	"""

	# Log out user if already logged in
	if current_user.is_authenticated():
	    logout_user()

	form = LoginForm()

	if request.method == 'POST' and form.validate():

		# Check the configuration file for user ids and passwords. This could
		# have been done using an LDAP or database backend.
		if request.form['username'] in valid_users:

			username = request.form['username']

			if request.form['password'] == valid_users[username]['password']:

				# Set the 'remember me' cookie?
				remember = False
				if 'remember' in request.form:
					remember = True

				user = User(id=username)
				login_user(user, remember)
				flash("Hello, %s!" % valid_users[username]['name'])
				return redirect(url_for("index"))

			else:
				flash("Bad password dude")

	return render_template("forms/login.html", form=form)


@app.route("/logout")
def logout():
	""" Log out the user if they're logged in
	"""
	if current_user.is_authenticated():
	    logout_user()
	return redirect(url_for("index"))
