import os
from flask import Flask
import pycurl
import cStringIO
import simplejson as json
import urllib

api_token = os.environ['CH_API_KEY']

app = Flask(__name__)

@app.route('/')
def iscooperhewittopen():
	if checkStatus() != '0':
		return "YES!"
	else:
		return "NO!"


def checkStatus():
	buf = cStringIO.StringIO()

	c = pycurl.Curl()
	c.setopt(c.URL, 'https://api.collection.cooperhewitt.org/rest')
	d = {'method':'cooperhewitt.galleries.isOpen','access_token':api_token}

	c.setopt(pycurl.SSL_VERIFYPEER, 0)   
	c.setopt(pycurl.SSL_VERIFYHOST, 0)

	c.setopt(c.WRITEFUNCTION, buf.write)

	c.setopt(c.POSTFIELDS, urllib.urlencode(d) )
	c.perform()

	rsp = json.loads(buf.getvalue())

	buf.reset()
	buf.truncate()

	status = rsp.get('open', [])
	status = str(status)
	
	return status
