from http.server import HTTPServer, BaseHTTPRequestHandler 
content="""
<html>
    <head>
        <title>WEB APPLICATION</title>
    </head>
    <body>
        <table border="6" bgcolor="lightyellow">
            <caption>OSI MODEL LAYERS</caption>
            <tr bgcolor="lightgreen">
                <th>S.no</th>
                <th>Layer</th>
                <th>Description</th>
            </tr>
            <tr>
                <td>1.</td>
                <td>Application</td>
                <td>User interface, network services</td>
            </tr>
            <tr>
                <td>2.</td>
                <td>Presentation</td>
                <td>Data translation, encryption</td>
            </tr>
            <tr>
                <td>3.</td>
                <td>Session</td>
                <td>Establishes, manages sessions</td>
            </tr>
            <tr>
                <td>4.</td>
                <td>Transport</td>
                <td>Reliable data transfer</td>
            </tr>
            <tr>
                <td>5.</td>
                <td>Network</td>
                <td>Routing, addressing</td>
            </tr>
            <tr>
                <td>6.</td>
                <td>Data Link</td>
                <td>MAC addressing, error detection</td>
            </tr>
            <tr>
                <td>7.</td>
                <td>Physical</td>
                <td>Bit transmission through media</td>
            </tr>
        </table>
    </body>
</html>

"""
class myhandler (BaseHTTPRequestHandler):
     def do_GET(self):
        print("request received") 
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('', 8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()