# @authors:
#       redm7920
#       oged9220

from socket import *
import sys
from multiprocessing import *

BUFF_SIZE = 4096


def handler(clientSocket, address):
    message = clientSocket.recv(BUFF_SIZE).decode()

    print(message)

    # Extract the filename from the given message
    file_to_use = message.split()[1]
    url = message.split()[1].partition("/")[2]

    if "/" in url:
        url = url.replace("/", "")
    print(url)

    if "favicon" in url:
        print("FAVICON REJECT PLZ")
        return None

    file_handler(file_to_use, url, clientSocket)


def file_handler(file_to_use, url, cliSock):
    fileExist = "false"
    try:
        print("[*]CHECKING CACHE FOR FILE [*]")
        f = open("cache" + file_to_use, "r", encoding="utf8")
        outputdata = f.readlines()
        fileExist = "true"

        # ProxyServer finds a cache hit and generates a response message
        cliSock.send(b"HTTP/1.0 200 OK\r\n")
        cliSock.send(b"Content-Type:text/html\r\n")

        print('[*] Reading from cache [*]')
        for i in range(0, len(outputdata)):
            cliSock.send(outputdata[i].encode())

    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":

            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)

            hostn = "www." + url
            try:
                # Connect to port 80 on server
                c.connect((hostn, 80))
                print("CONNECTED TO {} ON PORT {}".format(hostn, '80'))

                # Create a temporary file on this socket and ask port 80
                # for the file requested by the client
                fileobj = c.makefile('rwb', 0)

                req = "GET / HTTP/1.1\r\nHost: " + url + "\r\n\r\n"
                fileobj.write(req.encode(encoding="utf8"))

                # Read the response into buffer
                buffer = fileobj.readlines()

                status_code = buffer[0].split()
                if status_code[1] == b'200':
                    # Create a new file in the cache for the requested file.
                    # Also send the response in the buffer to client socket
                    # and the corresponding file in the cache
                    tmpFile = open("cache/" + url, "wb")

                    for line in buffer:
                        # print("[*] ", line)
                        tmpFile.write(line)
                        cliSock.send(line)

                elif status_code[1] == b'301':
                    print("ERROR 301\n")
                    cliSock.send(b"HTTP/1.1 200 OK\r\n")
                    cliSock.send(b"Content-Type:text/html\r\n")
                    cliSock.send(b"<html><body><h1>ERROR 301</h1><br><h3>Please try again</h3></body></html>")

                elif status_code[1] == b'302':
                    print("ERROR 302\n")
                    tmpFile = open("cache/" + url, "wb")
                    for i in buffer:
                        tmpFile.write(i)
                        cliSock.send(i)

                elif status_code[1] == b'400':
                    print("ERROR 400\n")
                    cliSock.send(b"HTTP/1.0 200 OK\r\n")
                    cliSock.send(b"Content-Type:text/html\r\n")
                    cliSock.send(b"<html><body><h1>ERROR 400</h1><br><h3>Please try again</h3></body></html>")

                elif status_code[1] == b'404':
                    print("ERROR 404\n")
                    cliSock.send(b"HTTP/1.0 200 OK\r\n")
                    cliSock.send(b"Content-Type:text/html\r\n")
                    cliSock.send(b"<html><body><h1>ERROR 404</h1><br><h3>Please try again</h3></body></html>")

                elif status_code[1] == b'500':
                    print("ERROR 500\n")
                    cliSock.send(b"HTTP/1.0 200 OK\r\n")
                    cliSock.send(b"Content-Type:text/html\r\n")
                    cliSock.send(b"<html><body><h1>ERROR 500</h1><br><h3>Please try again</h3></body></html>")

                else:
                    print("FIRST BUFFER LINE: ", buffer[0])

                c.close()

            except error as e:
                print(e)
                print("Illegal request")
                cliSock.send(b"HTTP/1.0 200 OK\r\n")
                cliSock.send(b"Content-Type:text/html\r\n")
                cliSock.send(b"<html><body><h1>ILLEGAL REQUEST</h1><br><h3>Please try again</h3></body></html>")
        else:
            # HTTP response message for file not found
            # Fill in start.
            # Fill in end.
            cliSock.send(b"HTTP/1.0 200 OK\r\n")
            cliSock.send(b"Content-Type:text/html\r\n")
            cliSock.send(b"<html><body><h1>ILLEGAL REQUEST</h1><br><h3>Please try again</h3></body></html>")

    # Close the client socket
    cliSock.close()


def main(serverSocket):

    print("~ PROGRAM START ~")

    while 1:
        # Strat receiving data from the client
        print('[*] Ready to serve...\n')
        clientSocket, addr = serverSocket.accept()
        print('\n\n[*] Received a connection from:', addr)

        process = Process(target=handler, args=(clientSocket, addr))
        process.start()
        active_children()


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('Usage : python proxy.py server_port\n')
        sys.exit(2)

    # Create a server socket, bind it to a port and start listening
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', int(sys.argv[1])))
    serverSocket.listen(1)

    main(serverSocket)

    serverSocket.close()
