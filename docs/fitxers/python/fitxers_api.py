## https://jsonplaceholder.typicode.com/
## https://jsonplaceholder.typicode.com/users/1
import socket

server_addr = "jsonplaceholder.typicode.com"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

sock.connect((server_addr, 80))

que_volem = b"/users/2"
sock.send(b"GET " + que_volem + b" HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")

reply = sock.recv(10000)

sock.shutdown(socket.SHUT_RDWR)
sock.close()
