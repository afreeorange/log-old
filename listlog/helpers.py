from datetime import datetime
import lxml.html
from listlog import app
list_of_post_types = app.config['POST_TYPES']


@app.template_filter('relative_date')
def relative_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time,datetime):
        diff = now - time 
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return  "a minute ago"
        if second_diff < 3600:
            return str( second_diff / 60 ) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str( second_diff / 3600 ) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        return str(day_diff/7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff/30) + " months ago"
    return str(day_diff/365) + " years ago"


@app.template_filter('expand_post_type')
def expand_post_type(post_type):
    """ Return the human-readable version of the post type
    """
    for index, types in enumerate(list_of_post_types):
        if types[0] == post_type:
            return list_of_post_types[index][1]


def get_url_title(the_url):
    """ A very basic title grabber. Could've used BeautifulSoup
    """
    return lxml.html.parse(the_url).find(".//title").text


def enforce_integer(the_number):
    """ Guard against nefariousness. Either return a positive
        integer or 1. Wanted to round floats, but meh...
    """
    try:
        the_number = int(the_number)
    except ValueError, e:
        return 1
    else:
        if the_number == 0 or the_number < 0:
            return 1
        else:
            return the_number
