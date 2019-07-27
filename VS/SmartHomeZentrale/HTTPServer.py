import socket
import threading

class HTTPServer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.TCP_IP = '127.0.0.1'
        self.TCP_PORT = 4444
        self.BUFFER_SIZE = 1024

    def processRequest(self, inFromClient):
        cut = inFromClient.find(" HTTP")
        request = inFromClient[2:cut]
        cut = inFromClient[0:20].find("&")
        if (cut > 0):
            param = int(inFromClient[cut:inFromClient.find(" ")])
            #print("param: " + param)
            requestdict = {'request': request, 'param': param}
            #print(request)
            #print(param)
            return requestdict
        else:
            requestdict = {'request': request}
            return requestdict

    def createResponse(self, requestdict):
        if (requestdict["request"] == "GET /"):
            f = open("Sensordaten.txt", "r")
            response = ""
            for line in f:
                response = response + line + "<br>"
            return response
        else:
            return "404 Page not Found"
            
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.TCP_IP, self.TCP_PORT))
        sock.listen(1)
        print("HTTP Server wurde gestartet...")
        
        while True:
            conn, addr = sock.accept()
            data = self.processRequest(str(conn.recv(self.BUFFER_SIZE)))
            response = str(self.createResponse(data))
            conn.send(str.encode("HTTP/1.1 200 OK \n content-Type:text/html\n\n"
                        + "<html><head><title>Verteilte Systeme</title></head><body><p>"
                        + response
                        + "</p></body></html>"))
