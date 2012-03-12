import json
import pdb
import pycurl
import Queue
import sys
import threading
import twitter
import urllib

def on_receive(data):  
    global datalock
    #  print "Received tweet from twitter!"
    global databuffer
    global NEWTWITTERDATA
    if not datalock.acquire():
        pdb.set_trace()
    databuffer = databuffer + data
    datalock.release()
    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'code': NEWTWITTERDATA}))


class GetTwitterData(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.STREAM_URL = "http://search.twitter.com/search.json?lang=en&geocode=&q=&rpp=1&page="
		self.pagecount = 1;
		self.working = False
		self.conn = pycurl.Curl()
		self.conn.setopt(pycurl.WRITEFUNCTION, on_receive)  
		self.daemon = True
		
		self.query = "obama"
		self.location = "52,0,100mi"
	def run(self):
		global TWITTERCONNECTIONLOST
		global databuffer
		global datalock
		global toClassQueue
		while True:
			if toClassQueue.qsize() > 10:
				pygame.time.wait(1000)
				continue
			if not self.working:
				self.pagecount = 1
				pygame.time.wait(100)
				continue
			try:
				url = self.STREAM_URL[0:54] + self.location + self.STREAM_URL[54:57] + self.query + self.STREAM_URL[57:] + str(self.pagecount)
				self.conn.setopt(pycurl.URL, url)
				self.conn.perform()
				if not self.working :
					continue
				if not datalock.acquire():
					pdb.set_trace()
				databuffer = databuffer + "\n"
				datalock.release()
				pygame.time.wait(50)
				self.pagecount = self.pagecount + 1
			except Exception:
				pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'code': TWITTERCONNECTIONLOST}))
