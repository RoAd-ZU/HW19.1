from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):

    def get_content(self):
        with open('hw19_1.html', 'r', encoding="utf-8") as f:
            r = f.read()
        return f"""{r}"""
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        query_comp = parse_qs(urlparse(self.path).query)
        print(query_comp)
        self.content = self.get_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(self.content, "utf-8"))

if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:

        webServer.serve_forever()
    except KeyboardInterrupt:
        pass


    webServer.server_close()
    print("Server stopped.")