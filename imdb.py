#!/usr/bin/env python27

import urllib2
import re
import json

movie = raw_input("Enter Movie: ")
value = re.compile(r' ')
movie_add = value.sub('+', movie) #replace ' ' with '+'
print movie_add

url = "http://www.imdbapi.com/?t=" + movie_add

conn = urllib2.Request(url)
result = json.load(urllib2.urlopen(conn))
print json.dumps(result)