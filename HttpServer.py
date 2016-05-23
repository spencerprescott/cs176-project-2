import socket
import select
import Queue
from Routing import Router
import Controllers

class HttpServer(object):
	"""
	Simple Http Server that listens for requests on the port provided
	"""

	def __init__(self, router):
		super(HttpServer, self).__init__()
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.socket.setblocking(0)
		self.router = router

	def listen(self, port):
		"""
		Binds socket to a port on localhost and 127.0.0.1
		Listens for HTTP Requests and responds
		"""
		self.socket.bind(("127.0.0.1", port))
		self.socket.listen(5)
		print("Listening on 127.0.0.1:" + str(port))
		self.inputs = [self.socket]
		self.outputs = []
		self.message_queues = {}
		self.message_entireties = {}
		while self.inputs:
			readable, writable, exceptional = select.select(self.inputs, self.outputs, self.inputs)
			for s in readable:
				if s is self.socket:
					connection, client_address = s.accept()
					print("Connection from: " + str(client_address[0]) + ":" + str(client_address[1]))
					connection.setblocking(0)
					self.inputs.append(connection)
					self.message_queues[connection] = Queue.Queue()
				else:
					data = s.recv(1024)
					if data:
						# a readable client socket has data
						self.message_queues[s].put(data)
						# add output channel for response
						if s not in self.outputs:
							self.outputs.append(s)
					else:
						# Interpret empty results as closed connection
						# Stop listening for input on the connection
						self.close(s)
			for s in writable:
				try:
					next_msg = self.message_queues[s].get_nowait()
					if s in self.message_entireties:
						self.message_entireties[s] = self.message_entireties[s] + next_msg
					else:
						self.message_entireties[s] = next_msg
				except Queue.Empty:
					# No messages waiting, so stop checking for writability
					self.outputs.remove(s)
				else:
					if self.message_entireties[s].endswith("\n\n") or self.message_entireties[s].endswith("\r\n\r\n"):
						self.router.handleRequest(s, self.message_entireties[s])
						self.close(s)
			for s in exceptional:
				# if there is an error with a socket, it is closed
				self.close(s)

	def close(self, s):
		"""
		Stop listening and shut down server
		"""
		if s in self.outputs:
			self.outputs.remove(s)
		self.inputs.remove(s)
		s.close()
		# remove the message queue
		if s in self.message_queues:
			del self.message_queues[s]
		if s in self.message_entireties:
			del self.message_entireties[s]
