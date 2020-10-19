print ("HelloWorld")
import feedparser
from pprint import pprint

feed1 = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale')
pprint(feed1)
