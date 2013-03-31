import lxml.html

""" A very basic title grabber. Could've used BeautifulSoup
"""
def get_page_title(the_page):
    return lxml.html.parse(the_page).find(".//title").text
