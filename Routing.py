import Controllers
import socket
from Constants import *

class Router(object):
	"""
	Maps requests to handler controller methods
	"""
	def __init__(self):
		super(Router, self).__init__()
		self.routes = {}

	def addRoute(self, path, controller_with_method):
		""" 
		Maps the path (/names, /sort/*, etc.) parameter to a controller and method of the form Controller#method
		"""
		controller = controller_with_method.split("#")[0]
		method_string = controller_with_method.split("#")[1]
		instance = getattr(Controllers, controller)()
		method_call = getattr(instance, method_string)
		self.routes[path] = method_call

	def handleRequest(self, socket, request_string):
		"""
		Parses the HTTP Request and determines what to page to respond with and if applicable, the values to pass
		to the controller. For this situation it would be the values to sort
		"""
		# Get the uri: names, sort/1/4/2, etc.
		split_request = request_string.split("\n")[0].split(" ")
		if split_request[0].strip() != "GET" and split_request[0].strip() != "HEAD":
			socket.send(NOT_IMPLEMENTED_HEADER)
			return
		endpoint = split_request[1][1:]
		if endpoint in self.routes:
			# Easy map: there is a route in the routes dictionary that endpoint maps to,
			# this route also has no paramters, i.e. names or hello/world
			socket.send(self.routes[endpoint]())
			return
		else:
			# There is no direct mapping to this endpoint. So now loop through the declared routes and
			# see if there is a route with an * (meaning wildcard) and see if that route matches 
			# the endpoint exactly before the *. i.e. sort/1/3/2 to sort/* 
			for route in self.routes.keys():
				split_by_slash = route.split("/")
				for i in range(len(split_by_slash)):
					if split_by_slash[i] == "*":
						if endpoint.split("/")[:i] == split_by_slash[:i]:
							args = endpoint.split("/")[i:]
							trimmed_route = "/".join(endpoint.split("/")[:i])
							socket.send(self.routes[trimmed_route + "/*"](args))
							return
						continue

		# No route exist, respond with 404
		socket.send(NOT_FOUND)
		
			
