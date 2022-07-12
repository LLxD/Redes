from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        filename = './index.html'
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fh:
            html = fh.read()
            self.wfile.write(html)
        print("Thread Atual -> " + threading.currentThread().getName())
        return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Lida com as threads em uma thread separada."""


if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 6789), RequestHandler)
    print('Iniciando servidor em http://localhost:6789, use Ctrl-C para encerrar')
    server.serve_forever()
