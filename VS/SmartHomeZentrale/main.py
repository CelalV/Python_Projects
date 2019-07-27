import UDP_Server
import HTTPServer

def main():

    udpServer = UDP_Server.UDPServer()
    udpServer.start()

    httpserver = HTTPServer()
    httpserver.start()
