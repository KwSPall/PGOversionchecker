import urllib
import sys
import time
# from lxml import html

page = ""

def get_string_from_page(str_begin, str_end):
	"gets a first match between begin and end, then moves page to the end. call only if found str_begin"
	global page
	pos = page.find(str_begin)
	page = page[pos + len(str_begin):]
	end = page.find(str_end)
	res = page[0:end]
	page = page[end:]
	return res

def print_version(version, rel_date):
	print version, " released on ", rel_date	

version_tag = "<span class=\"infoslide-name\">Version:</span><span class=\"infoslide-value\">"
date_tag = "<span class=\"infoslide-name\">Uploaded:</span><span class=\"infoslide-value\"><span style=\"\" class=\"datetime_utc\" data-utcdate=\""
version_end = "</span>"
date_end = "\">"
url = "http://www.apkmirror.com/apk/niantic-inc/pokemon-go/"

print "Getting page... please wait"
page = urllib.urlopen(url).read()

while (page.find(version_tag) > 0):
	cur_version = get_string_from_page(version_tag, version_end)
	cur_date = get_string_from_page(date_tag, date_end)
	print_version(cur_version, cur_date)

