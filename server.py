#! /usr/bin/python
import socket
import argparse
from functools import reduce
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
s.bind((host, port))
s.listen(1)

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    data = conn.recv(2048)
    if not data: break

    # Convert input into a list of integers
    num_list = list(map(lambda x: int(x), data.decode("utf-8").split( )))

    # Use reduce to compute sum of list
    num_sum = reduce((lambda x, y: x + y), num_list)

    # Convert sum to bytes and send to client
    conn.sendall(num_sum.to_bytes(2, byteorder='big'))
    
conn.close()
