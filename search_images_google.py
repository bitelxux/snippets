#!/usr/bin/python

import urllib
import mechanize
import cookielib
import re
import sys
import ConfigParser

class Search():

    def __init__(self):
        self.setup_con()

    def setup_con(self):

        # Browser
        self.br = mechanize.Browser()

        # Cookie Jar
        self.cj = cookielib.LWPCookieJar()
        self.br.set_cookiejar(self.cj)

        # Browser option
        self.br.set_handle_equiv(True)
        self.br.set_handle_gzip(True)
        self.br.set_handle_redirect(True)
        self.br.set_handle_referer(True)
        self.br.set_handle_robots(False)

        # Follows refresh 0 but not hangs on refresh > 0
        self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        # Want debugging messages?
        #br.set_debug_http(True)
        #br.set_debug_redirects(True)
        #br.set_debug_responses(True)

        # User-Agent (this is cheating, ok?)
        self.br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    def search(self, what):

        self.site = "https://www.google.ie/search?q={}&biw=1920&bih=965&source=lnms&tbm=isch&sa=X&sqi=2&ved=0ahUKEwjemJvzrMvPAhUoJcAKHa0eBfoQ_AUIBigB".format(what)

        r = self.br.open(self.site)
        info = r.info()
        html = r.read()

        images = []
        p = '(?<=src=").*?(?=")'
        for m in re.finditer(p, html):
            images.append(html[m.start():m.end()])

        return images

if __name__ == "__main__":
   search = Search()
   images = search.search("shark")
   for image in images:
       print image
   


