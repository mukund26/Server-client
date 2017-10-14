#! /usr/bin/python
import socket
import argparse

# Initialize argument parser
parser = argparse.ArgumentParser()

# Command line argument for Server Address
# If left blank defaults to 127.0.0.1
parser.add_argument("Host",
                    help="Enter the host",
                    type=str,
                    nargs="?",
                    const=1,
                    default="127.0.0.1")

# Command line argument for Port Number
# If left blank defaults to 12345
parser.add_argument("Port",
                    help="Enter the port",
                    type=int,
                    nargs="?",
                    const=1,
                    default=12345)

host = parser.parse_args().Host
port = parser.parse_args().Port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Take input from a user, encode it to utf-8, and send to server
a =input("Enter space-separated integers: -\n")
s.sendall(a.encode("utf-8"))

data = s.recv(1024)
s.close()
# Convert received data from bytes to integers
print("Received data: ", int.from_bytes(data, byteorder='big'))
