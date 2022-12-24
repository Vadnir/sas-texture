from http.server import HTTPServer, BaseHTTPRequestHandler

port = 44440

url = "https://websockets.readthedocs.io/en/stable/intro/index.html"


class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(302)
       self.send_header('Location', url)
       self.end_headers()


HTTPServer(("", port), Redirect).serve_forever()
