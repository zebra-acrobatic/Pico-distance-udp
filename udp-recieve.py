# This is a simple script to liseten for UDP messages.
import socket

# Define the IP address and port to listen on
UDP_IP = "0.0.0.0"  # Listen on all available network interfaces
UDP_PORT = 12345    # Port to listen on (Replace with your port of choice)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the IP address and port
sock.bind((UDP_IP, UDP_PORT))

print("UDP server is running...")

# Listen for incoming UDP packets
while True:
    # Receive data from the client
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes

    # Print received data and client address
    print("Received message from", addr, ":", data.decode("utf-8"))  # Assuming UTF-8 encoding
