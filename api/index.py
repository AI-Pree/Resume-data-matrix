from http.server import BaseHTTPRequestHandler
from urllib import parse
import qrcode
from cowpy import cow

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        user_path = self.path
        parse_path = dict(parse.parse_qsl(parse.urlsplit(user_path).query))
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )


        message = cow.Cowacter().milk('Hello from Python from a Serverless Function!')
        self.wfile.write(message.encode())
        return
