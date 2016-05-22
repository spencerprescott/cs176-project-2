from HttpServer import *
from Routing import Router

#TODO: Get port # from command line

if __name__ == '__main__':
	router = Router()
	router.addRoute("names", "NamesController#index")
	router.addRoute("sort/*", "SortController#sort")
	HttpServer(router).listen(8000)