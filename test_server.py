from http.server import BaseHTTPRequestHandler, HTTPServer
from pydantic import BaseModel, ValidationError
import requests
import json


HOST = "localhost"
PORT = 8000


class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    phone: str
    website: str


class Handler(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):

        self.send_response(status)

        self.send_header(
            "Content-Type",
            "application/json"
        )

        self.end_headers()

        self.wfile.write(
            json.dumps(
                data,
                indent=2
            ).encode("utf-8")
        )

    def do_GET(self):

        if self.path == "/":

            self.send_json({
                "message": "Server running"
            })

        elif self.path == "/api/user":

            try:

                url = (
                    "https://jsonplaceholder."
                    "typicode.com/users/1"
                )

                response = requests.get(
                    url,
                    timeout=5
                )

                response.raise_for_status()

                raw_data = response.json()

                # Validate + select required fields
                user = User.model_validate(
                    raw_data
                )

                self.send_json(
                    user.model_dump(),
                    200
                )

            except ValidationError as e:

                self.send_json(
                    {
                        "error":
                        "Invalid API data",

                        "details":
                        e.errors()
                    },
                    422
                )

            except requests.RequestException as e:

                self.send_json(
                    {
                        "error":
                        "Failed to fetch API",

                        "details":
                        str(e)
                    },
                    500
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