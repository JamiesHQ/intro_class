import urllib2
import json
from api_keys import *

url_base = 'http://api.wunderground.com/api/' + MY_WEATHERUNDERGROUND_KEY

def get_temp_in(city, state_abbrev):
	f=urllib2.urlopen(url_base +)