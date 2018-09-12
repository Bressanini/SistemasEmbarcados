import sys
import BaseHTTPServer
import datetime

from SimpleHTTPServer import SimpleHTTPRequestHandler


HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8080
server_address = ('0.0.0.0', port)
dateTime = datetime.datetime.now().time()
dateTime2 = datetime.datetime.now().time()
html = "<!DOCTYPE html>  \
		<html> \
			<body> \
				<h1>System Information</h1> \
				<p>Local Data: {code}</p> \
				<p>Local Data: {code2}</p> \
				<p>s</p> \
			</body> \
		</html>".format(code=dateTime,code2=dateTime)


f = open("index.html", "w")
f.write(html)
f.close()

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()
