#! /usr/bin/python
import socket
from functools import reduce

host = "127.0.0.1"
port = 12345

# Create a server a bind to port 12345 on localhost
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    data = conn.recv(1024)
    if not data: break

    # Convert input into a list of integers
    num_list = list(map(lambda x: int(x), data.decode("utf-8").split(' ')))

    # Use reduce to compute sum of list
    num_sum = reduce((lambda x, y: x + y), num_list)

    # Convert sum to bytes and send to client
    conn.sendall(num_sum.to_bytes(2, byteorder='big'))
conn.close()
