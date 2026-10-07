from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "localhost"
PORT = 8000


class Handler(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        response = json.dumps(data)

        self.wfile.write(
            response.encode("utf-8")
        )

    def do_GET(self):

        if self.path == "/":

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(
                b"Server is running!!!"
            )

        elif self.path == "/hello":

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(
                b"Hello from Python API"
            )

        elif self.path == "/api/user":

            data = {
                "name": "Aditya",
                "role": "Student",
                "status": "active"
            }

            self.send_json(data, 200)

        else:

            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(
                b"Endpoint not found"
            )

    def do_POST(self):

        if self.path == "/api/user":

            content_length = int(
                self.headers.get(
                    "Content-Length",
                    0
                )
            )

            body = self.rfile.read(
                content_length
            )

            data = json.loads(
                body.decode("utf-8")
            )

            print(
                "Received Data:",
                data
            )

            response = {
                "message": "User received",
                "user": data
            }

            self.send_json(
                response,
                201
            )

        else:

            self.send_json(
                {
                    "error":
                    "Endpoint not found"
                },
                404
            )


server = HTTPServer(
    (HOST, PORT),
    Handler
)

print(
    f"Server running at "
    f"http://{HOST}:{PORT}"
)

server.serve_forever()