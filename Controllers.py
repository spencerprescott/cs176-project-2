from Constants import *

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
		res = ok_header("text/plain")
		for value in values:
			res += str(value) + " "
		return res

class NamesController(object):
	"""
	Controller class that handles the request for the names endpoint
	"""
	def __init__(self):
		super(NamesController, self).__init__()

	def index(self):
		#TODO: Add content length and date
		return ok_header() + """<!DOCTYPE html>
				<html>
				<head>
				 <title>names</title>
				</head>
				<body>
				 <p>Spencer Prescott, 3270709</p>
				 <p>Name 2, PERM 2</p>
				</body>
				</html>"""