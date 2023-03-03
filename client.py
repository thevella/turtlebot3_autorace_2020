import socket
import sys
import pickle
import data_structures as ds

# https://docs.python.org/3/library/socketserver.html

HOST, PORT = "localhost", 60123
data = {0:True}

pick_data = pickle.dumps(data)

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(pick_data)


print("Sent:     {}".format(data))