from flask import render_template, request, flash, redirect, url_for
from listlog import app, login_manager
from models import LoginForm, User
from flask.ext.login import login_user, logout_user, login_required, current_user

# Achieved largely using these:
# http://pythonhosted.org/Flask-Login/#how-it-works
# and then: 
# http://stackoverflow.com/a/12081788


@login_manager.user_loader
def load_user(userid):
	""" Return the user object.
	"""
	return User(id=app.config['USER']['id'])


@app.route("/login", methods=['GET', 'POST'])
def login():
	""" Log in a valid user.
	"""

	# Log out user if already logged in
	if current_user.is_authenticated():
	    logout_user()

	form = LoginForm()

	if request.method == 'POST' and form.validate():

		# Check the configuration file for the user id and password. This could
		# have been done using an LDAP or database backend.
		if request.form['username'] == app.config['USER']['id'] and request.form['password'] == app.config['USER']['password']:

			# Set the 'remember me' cookie?
			remember = False
			if 'remember' in request.form:
				remember = True

			user = User(id=request.form['username'])
			login_user(user, remember)
			flash("Hello, %s!" % app.config['USER']['name'])
			return redirect(url_for("index"))

	return render_template("forms/login.html", form=form)


@app.route("/logout")
def logout():
	""" Log out the user if they're logged in
	"""
	if current_user.is_authenticated():
	    logout_user()
	return redirect(url_for("index"))
