# EX01 Developing a Simple Webserver
## Date: 09/04/2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler 
content="""
<html>
<head>
    <title>TCP/IP Layers and Protocols</title>
</head>
<body>
    <table border="1" cellspacing="5" cellpadding="10">
        <tr>
            <th colspan="2">TCP/IP Layers</th>
            <th colspan="5">TCP/IP Protocols</th>
        </tr>

        <!-- Application Layer -->
        <tr bgcolor="#f2b6b6">
            <td rowspan="4"><strong>Application Layer</strong></td>
            <td></td>
            <td>HTTP</td>
            <td>FTP</td>
            <td>Telnet</td>
            <td>SMTP</td>
            <td>DNS</td>
        </tr>

        <!-- Transport Layer -->
        <tr bgcolor="#c2f0c2">
            <td><strong>Transport Layer</strong></td>
            <td colspan="2">TCP</td>
            <td colspan="3">UDP</td>
        </tr>

        <!-- Network Layer -->
        <tr bgcolor="#b3d9ff">
            <td><strong>Network Layer</strong></td>
            <td>IP</td>
            <td>ARP</td>
            <td>ICMP</td>
            <td colspan="2">IGMP</td>
        </tr>

        <!-- Network Interface Layer -->
        <tr bgcolor="#f9e79f">
            <td><strong>Network Interface Layer</strong></td>
            <td>Ethernet</td>
            <td>Token Ring</td>
            <td colspan="3">Other Link-Layer Protocols</td>
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

```

## OUTPUT:
![Screenshot 2025-04-21 165816](https://github.com/user-attachments/assets/29d0fbfe-ed72-4234-978f-afea600c74f3)

![alt text](<Screenshot 2025-04-09 144309.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
