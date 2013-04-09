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
		return weOpen
	else:
		return weClosed


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

weOpen = """
<!DOCTYPE html>
<!--[if IE]><![endif]-->
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="description" content="Is Cooper-Hewitt Open? Find out here." />
    <meta name="application-name" content="Is Cooper-Hewitt Open?" />
    <meta name="msapplication-tooltip" content="Is Cooper-Hewitt Open?" />
    <meta name="author" content="Micah Walter" />
    <meta http-equiv="imagetoolbar" content="false" />


    <title>Is Cooper-Hewitt Open?</title>

    <link href="static/style.css" media="all" rel="stylesheet" type="text/css" />
    <!--[if lt IE 9]>
        <script src="http://ie7-js.googlecode.com/svn/version/2.1(beta4)/IE9.js"></script>
        <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
  </head>
  <body>
    <header>
      <h1>Is Cooper-Hewitt Open?</h1>
    </header>
    <section id="status">
      <h2>
        YUP!
      </h2>
    </section>
  </body>
</html>
"""

weClosed = """
<!DOCTYPE html>
<!--[if IE]><![endif]-->
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="description" content="Is Cooper-Hewitt Open? Find out here." />
    <meta name="application-name" content="Is Cooper-Hewitt Open?" />
    <meta name="msapplication-tooltip" content="Is Cooper-Hewitt Open?" />
    <meta name="author" content="Micah Walter" />
    <meta http-equiv="imagetoolbar" content="false" />


    <title>Is Cooper-Hewitt Open?</title>

    <link href="static/style.css" media="all" rel="stylesheet" type="text/css" />
    <!--[if lt IE 9]>
        <script src="http://ie7-js.googlecode.com/svn/version/2.1(beta4)/IE9.js"></script>
        <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
  </head>
  <body>
    <header>
      <h1>Is Cooper-Hewitt Open?</h1>
    </header>
    <section id="status">
      <h2>
        NOPE!
      </h2>
    </section>
  </body>
</html>
"""