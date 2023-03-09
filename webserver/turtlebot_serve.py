import socket
import sys
import pickle
import data_structures as ds
from data_structures import Commands, Command

# command_map = {Commands.CAMERA_PUBLISH: Command("roslaunch turtlebot3_autorace_camera raspberry_pi_camera_publish.launch").make_option("rate", 20),
#                Commands.PI_BRINGUP: Command("roslaunch turtlebot3_bringup turtlebot3_robot.launch")
#                }

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