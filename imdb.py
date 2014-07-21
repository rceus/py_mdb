#!/usr/bin/env python27

import urllib2
import re
import json
import sys
from termcolor import colored, cprint

movie = raw_input("Enter Movie: ")
value = re.compile(r' ')
movie_add = value.sub('+', movie) #replace ' ' with '+'
cprint (movie_add, 'green')

url = "http://www.imdbapi.com/?t=" + movie_add

conn = urllib2.Request(url)
result = (json.load(urllib2.urlopen(conn)))
print json.dumps(result)