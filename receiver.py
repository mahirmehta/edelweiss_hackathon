import socket
from data_processing import process_data_from_output as process_data


# Define the host and port to bind
host = 'localhost'
port = 9011

# Create a socket object
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
receiver_socket.bind((host, port))

# Listen for incoming connections
receiver_socket.listen(1)

# Set the number of entries to process
num_entries = 50

while True:
    # Accept a connection from a sender
    sender_socket, sender_address = receiver_socket.accept()

    try:
        # Receive the data
        data = sender_socket.recv(1024).decode()

        # Process the received data
        processed_data = process_data(data, num_entries)

        # Print the processed data
        print(processed_data)

    finally:
        # Close the sender socket connection
        sender_socket.close()
