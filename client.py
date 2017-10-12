#! /usr/bin/python
import socket

host="127.0.0.1"
port=12345

# Connect to port 12345 on localhost
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

# Take input from a user, encode it to utf-8, and send to server
a = input("Enter space-separated integers: -\n")
s.sendall(a.encode("utf-8"))

data = s.recv(1024)
s.close()

# Convert received data from bytes to integers
print("Received data: ", int.from_bytes(data, byteorder='big'))
