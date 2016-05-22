from Constants import *
import sys

class SortController(object):
	"""
	Controller class that handles the request for the sorting endpoint
	"""
	def __init__(self):
		super(SortController, self).__init__()

	def sort(self, values=[]):
		if len(values) > 0:
			converted_list = []
			for x in values:
				try:
					converted_list.append(int(x))
				except Exception, e:
					return NOT_FOUND
			converted_list.sort()
			values = converted_list
		#TODO: Add content length and date
		res = ""
		for value in values:
			res += str(value) + " "
		header = ok_header("text/plain", sys.getsizeof(res))
		return header + res

class NamesController(object):
	"""
	Controller class that handles the request for the names endpoint
	"""
	def __init__(self):
		super(NamesController, self).__init__()

	def index(self):
		#TODO: Add content length and date
		string_response =  """<!DOCTYPE html>
				<html>
				<head>
				 <title>names</title>
				</head>
				<body>
				 <p>Spencer Prescott, 3270709</p>
				 <p>Alok Gupta, 3579489</p>
				</body>
				</html>"""
		content_length = sys.getsizeof(string_response)
		return ok_header("text/html", content_length) + string_response
