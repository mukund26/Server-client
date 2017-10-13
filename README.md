# Server-client
Server-client is a simple application that demonstrates communication between a server and a client. 

## Use
- Execute server.py through the command line
```
python server.py <host_address> <port_number>
```
- Execute client.py through the command line
```
python client.py <host_address> <port_number>
```
- Input a list of space seperated integers into the client.py instance


## How it works
Running server.py creates an instance of the server which listens at port 12345. After the server is running, executing client.py will automatically establish a connection with the server. The client instance asks for data to be sent which needs to be a list of integers (>= 2 in length) seperated by spaces. The server splits the data into an array and computes the sum of the first and second element and returns it back to the client.
