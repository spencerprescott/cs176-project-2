import sys
from HttpServer import *
from Routing import Router
import pdb
from pdb import set_trace as bp


if __name__ == '__main__':
	try:
		port_number = sys.argv[1]
		router = Router()
		router.addRoute("names", "NamesController#index")
		router.addRoute("sort/*", "SortController#sort")
		HttpServer(router).listen(int(port_number))
	except:
		print "Error: Port number not included or invalid. Try again using a valid port. Run as 'python app.py [PORT]'"
