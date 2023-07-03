import subprocess
import socket

# Define the Java command
java_command = 'java -Ddebug=True -classpath feed-play-1.0.jar hackathon.player.Main dataset.csv 9011'

# Start the Java program as a subprocess
subprocess.Popen(java_command, shell=True)

# Wait for the Java program to start
# Sleep for a few seconds to allow the Java program to initialize
import time
time.sleep(2)

# Define the host and port to connect
host = 'localhost'
port = 9011

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Java program
client_socket.connect((host, port))

# Send any initial commands or data if needed
# client_socket.sendall("Initial command".encode())

# Receive the output from the Java program
output = client_socket.recv(1024).decode()
print('Output from Java program:', output)

# Close the socket connection
client_socket.close()