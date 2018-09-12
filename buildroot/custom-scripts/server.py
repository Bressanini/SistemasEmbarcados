import SimpleHTTPServer
import SocketServer
import os.path, sys
import datetime

#Formating string. The %s will be substituted by system data.
html = "<!DOCTYPE html>  \
		<html> \
			<body> \
				<h1>System Information</h1> \
				<p>Local Data: %s</p> \
			</body> \
		</html>"

#Handle de http requests.
class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	#Build the html file for every connection.
	def makeindex(self):
	    tofile = html % datetime.datetime.now().time()
		f = open("index.html", "w")
		f.write(html)
		f.close()
   return
	
	#Method http GET.	
	def do_GET(self):
		self.makeindex()
		self.path = '/index.html'
		return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

#Start the webserver.
Handler = MyRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', 8080), Handler)
server.serve_forever()
