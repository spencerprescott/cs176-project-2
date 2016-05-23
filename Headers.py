import time
from email.utils import formatdate

def get_time():
	return formatdate(timeval=None, localtime=False, usegmt=True)

str_response = """<!DOCTYPE html>
					<html>
					<head>
					 <title>404</title>
					</head>
					<body>
					 <h1>Error 404: Page Not Found</h1>
					</body>
					</html>"""
content_length = len(str_response.encode('utf-8'))

NOT_FOUND = """HTTP/1.0 404 Not Found\r\nContent-Type: text/html\r\nDate: """+ get_time() + """\r\nContent-Length: """ + str(content_length) + """\r\n\r\n""" + str_response

NOT_IMPLEMENTED_HEADER = "HTTP/1.0 501 Not Implemented\r\nContent-Type: text/html\r\nDate: " + get_time() + "\r\n\r\n"
def ok_header(text_type="text/html", content_length=0):
	return "HTTP/1.0 200 OK\r\nContent-Type: " + text_type + "\r\nContent-Length: " + str(content_length) + "\r\nDate: " + get_time() + "\r\n\r\n"
