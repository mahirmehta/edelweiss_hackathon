import socket
import pandas as pd

# Define the host and port to connect
host = 'localhost'
port = 9011

# Load the data into a DataFrame (replace this with your actual data loading logic)
data = pd.read_csv('dataset.csv')

# Convert DataFrame to a string representation
data_str = data.to_string(index=False)

# Create a socket object
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the receiver
    sender_socket.connect((host, port))

    # Send the data
    sender_socket.sendall(data_str.encode())

finally:
    # Close the socket connection
    sender_socket.close()
