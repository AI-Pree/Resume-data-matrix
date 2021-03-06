from http.server import BaseHTTPRequestHandler
from urllib import parse
import qrcode
import PIL
import io

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        user_path = self.path
        parse_path = dict(parse.parse_qsl(parse.urlsplit(user_path).query)) # parsing the url parameter passed by the user
        self.send_response(200)
        self.send_header('Content-type','image/png')
        self.end_headers()
        
        # parameters passed in the url path
        size = parse_path["size"]
        data = parse_path["data"]
        fill = parse_path["fill"]
        back = parse_path["bg"]
        
        # default QrCode configs
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=size,
            border=4,
        )

        qr.add_data(data)
        qr.make(fit=True)
        
        # generating the Qrcode image
        img = qr.make_image(fill_color=fill, back_color=back)

        # converting image to byte array for passing it to the client
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format="PNG")
        img_byte_array = img_byte_array.getvalue()

        self.wfile.write(img_byte_array)
        return
