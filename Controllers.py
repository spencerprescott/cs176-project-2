from Headers import *

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
		res = ""
		for value in values:
			res += str(value) + " "
		header = ok_header("text/plain", len(res.encode('utf-8')))
		return header + res

class NamesController(object):
	"""
	Controller class that handles the request for the names endpoint
	"""
	def __init__(self):
		super(NamesController, self).__init__()

	def index(self):
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
		content_length = len(string_response.encode('utf-8'))
		header = ok_header("text/html", content_length)
		header += string_response
		return header
