#!/bin/bash

# openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -subj "/" -keyout key.pem -out cert.pem

from http.server import HTTPServer, SimpleHTTPRequestHandler
from ssl import SSLContext, PROTOCOL_TLS_SERVER

host, port = '0.0.0.0', 4443
httpd = HTTPServer((host, port), SimpleHTTPRequestHandler)
ctx = SSLContext(PROTOCOL_TLS_SERVER)
ctx.check_hostname = False
ctx.load_cert_chain(certfile='cert.pem', keyfile="./key.pem")
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
try:
  print(f'Serving HTTPS on {host} port {port} (https://{host}:{port}/) ...')
  httpd.serve_forever()
except KeyboardInterrupt:
  print('Keyboard interrupt received, exiting.')
httpd.server_close()
