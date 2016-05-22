#TODO: Add content length and date
NOT_FOUND = """HTTP/1.0 404 Not Found\r\nContent-Type: text/html\r\n\r\n
				<!DOCTYPE html>
				<html>
				<head>
				 <title>404</title>
				</head>
				<body>
				 <h1>Page Not Found</h1>
				</body>
				</html>"""
NOT_IMPLEMENTED_HEADER = "HTTP/1.0 501 Not Implemented\r\nContent-Type: text/html\r\n\r\n"
def ok_header(text_type="text/html"):
	return "HTTP/1.0 200 OK\r\nContent-Type: " + text_type + "\r\n\r\n"