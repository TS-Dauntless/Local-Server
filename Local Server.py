from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import socket

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

location = input("Enter Directory Location to Serve(Leave Empty to serve the Current directory): ")
port = input("Enter Port(Leave Empty for port 5000): ")

if location == "":
    location = ".\\"

if port == "":
    port = 5000
else:
    port = int(port)


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=location, **kwargs)


with TCPServer((IPAddr, port), Handler) as server_:
    print(f"Server Started at {IPAddr}:{port}")
    server_.serve_forever()
