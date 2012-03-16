import urllib
import urllib2
import simplejson as json
import re

SEARCH_BASE = 'http://otter.topsy.com/search.json'
APP_ID = 'BB4FC86DF8674F76838FB55EED311689'

class Tweet:
    hits = 0
    author = ''
    content = ''
    def printTweet(self):
        #print ('Hits: ' + str(self.hits) + ' Author: ' + self.author + '\nTweet: ' + self.content + '\n')
        print self.content
        
def search(query, results_perpage=20, page_start = 1, mintime = 0, maxtime = 0,**kwargs):
    kwargs.update({
        'apikey': APP_ID,
        'q': query,
        'perpage': results_perpage,
        'page': page_start
    })
    if(mintime != 0):
        kwargs['mintime'] = mintime
        kwargs['maxtime'] = maxtime
    URL = SEARCH_BASE + '?' + urllib.urlencode(kwargs)
    print URL
    
    result = json.load(urllib.urlopen(URL))
    if 'Error' in result:
        # An error occurred; raise an exception
        print 'Error in json request'
        # raise YahooSearchError, result['Error']
    else:
        tweetList = []
        for tweet in result['response']['list']:
            t = Tweet()
            t.hits = tweet['hits']
            t.author = tweet['trackback_author_nick']
            t.content = tweet['content']
            t.content = t.content.replace('&quot;', '')
            t.content = t.content.replace('&amp;', '&')
            t.content = t.content.replace('&#39;', '\'')
            t.content = t.content.replace('&amp;', '\'')
            t.content = t.content.replace('\u2665', '')
            tweetList.append(t);
        return tweetList
    
