# @authors:
#       redm7920
#       oged9220

from socket import *
import sys

if len(sys.argv) <= 1:
    print("Usage : python client.py 'url'\n")
    sys.exit(2)

url = str(sys.argv[1])

cliSock = socket(AF_INET, SOCK_STREAM)

cliSock.connect((url, 80))

request = "GET / HTTP/1.1\r\nHost: " + url + "\r\n\r\n"

cliSock.sendall(request.encode())

response = cliSock.recv(4096)

print(response.decode())
