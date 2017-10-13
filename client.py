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
print("ENTER NO TO BE SENT:")
a = raw_input()
s.sendall(a)
data = s.recv(1024)
s.close()
print("RECEIVED DATA :", data)
