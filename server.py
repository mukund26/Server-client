#! /usr/bin/python
import socket
import argparse

parser = argparse.ArgumentParser()

# Command line argument for Server Address
# If left blank defaults to localhost
parser.add_argument("Host",
                    help="Enter the host",
                    type=str,
                    nargs="?",
                    const=1,
                    default="127.0.0.1")

# Command line argument for Port Number
# If left blank defaults to 8080
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
    print("Connected by:", addr)
    data = conn.recv(1024)
    if not data: break
    a = [int(i) for i in data.split(' ')]
    k = a[0] + a[1]
    k = str(k)
    conn.sendall(k)
conn.close
