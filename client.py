#! /usr/bin/python
import socket
import argparse

# Initialize argument parser
parser = argparse.ArgumentParser()

# Command line argument for Server Address
# If left blank defaults to 127.0.0.1
parser.add_argument("--host",
                    help="Enter the host",
                    dest="host",
                    type=str,
                    default="127.0.0.1")

# Command line argument for Port Number
# If left blank defaults to 12345
parser.add_argument("--port",
                    help="Enter the port",
                    dest="port",
                    type=int,
                    default=12345)

host = parser.parse_args().host
port = parser.parse_args().port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Take input from a user, encode it to utf-8, and send to server
a = input("Enter space-separated integers: -\n")
s.sendall(a.encode("utf-8"))

data = s.recv(2048)
s.close()
# Convert received data from bytes to integers
print("Received data: ", int.from_bytes(data, byteorder='big'))
