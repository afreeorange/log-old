ListLog
=======

Something like a single-user Tumblr. Mostly an attempt to teach myself Flask, Jinja2, MongoDB, and Bootstrap when I'm bored.

Prerequisites
-------------

* `virtualenv` somewhere in your `$PATH`
* A [running MongoDB instance](http://docs.mongodb.org/manual/installation/)

Installation
------------

* Edit `settings.py`.
* Run `install`. It's a bash script that should do most of the heavy lifting for you. Hopefully.

Usage 
-----

Simply run the `start` script. It'll start the project with three Gunicorn threads. Use the `stop` script to kill them. 

If you'd rather use flask,

	start flask

I've been messing around with Tornado as well

	start tornado

You can then log in with `admin` and `pass`

License
-------

MIT. See `LICENSE`