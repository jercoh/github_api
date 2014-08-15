import urllib2 as urllib
import re

_debug = 0
http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

def githubreq(url):

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, None)
  response_headers = response.info()

  link = response_headers.dict['link']
  next_url = re.search(r'\<([^>]*)\>', link).group(1)
  rel = re.search(r'rel=\"([^\"]*)\"', link).group(1)

  return response, next_url, rel

def fetchsamples():
  url = "https://api.github.com/repos/mbostock/d3/commits?sha=master&since=2013-01-01T00:00:00Z&until=2013-12-31T23:59:59"
  parameters = []
  response, next_url, rel = githubreq(url)
  while rel == 'next':
    for line in response:
      print line.strip()
    response, next_url, rel = githubreq(next_url)

if __name__ == '__main__':
  fetchsamples()
