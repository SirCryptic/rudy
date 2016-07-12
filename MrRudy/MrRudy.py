#!/usr/bin/env  python

import threading, urllib2, Queue
from sys import argv 
from time import sleep

# Tor class represents a thread-safe Tor connection with changeble cirtcuits  
class tor:
    def __init__(self):
        self.tor = ()
        self.ip_addr = '0.0.0.0'

    def changeIdentity(self):
        # Send a signal to Tor control port to change circuit / identity
        pass

    def send(self,data):

        # Send data through Tor Socks5 connection

        self.tor.send(data)

# Tor object thread queue. Inherited from Queue class
class torQ(Queue.Queue, object):
    def __init__(self):
        super(torQ, self).__init__()
    def push(self,torObject):
        super().put(torObject)
    def pop(self):
        return super().get()
        
# Signature evasion magic factory
class evasion:
    def __init__(self):
        self.TimeBetweenChars = 10 # Milliseconds
        self.TimeBetweenThreads = 100 # Milliseconds
        self.serverTimeout = 5 # Milliseconds
        self.serverVersion = "Apache"
        
    def getRandomString(self,numOfChars=10):

        #Return random chars at length specified
        pass
    
    def testServerTimeout(self):
        #Loop between default timeout setting downwards 
        #in sleep time to test server sensitivity level

        t = tor()
        timeout = self.serverTimeout
        for nap_time in range(timeout,1):
            try:
                t.send(self.getRandomString())
                sleep(nap_time)
                timeout = nap_time
            except:
                pass
        return timeout
    def getServerVersion(self):
        # Make request to server and get server type
        version = "Apache"
        self.serverVersion = version
        
# Find form fields and POST action
class parseHtmlForm():
    def __init__(self,FQDN='http://localhost/'):
        self.html = urllib2.urlopen(FQDN).read()
    def getHTML(self):
        pass
        # Get page contents from fully qualified domain name URL
    def findForm(self,html=self.html):
        pass
        # Find form elements in html, return dictionary with full POST actions and fields

# Open socks connection via Tor object
class connection():
    def __init__(self,target='',post_fields=[]):
        self.target = target
        self.post_fields = post_fields

if __name__ == "__main__":
    print "Hello traveler. This is Mr.Rudy"
