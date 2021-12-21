from http.server import BaseHTTPRequestHandler
from urllib import parse
from datetime import datetime
import platform

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        url_components = parse.urlunsplit(path)
        query_list = parse.parse_qsl(url_components)
        dic = dict(query_list)

        name = dic.get("name")
        date_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        if name:
            message = f"Hello {name}! Todays date and time is: {date_time}\n You are using Python version: {platform.python_version()}"
        else:
            message = "You are a stranger. No date and time available\n No Python version available. Enter a query name in the url!"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
