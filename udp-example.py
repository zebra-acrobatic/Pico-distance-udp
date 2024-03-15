# Simple UDP socket send message example
import socket as socket

# Create UDP socket
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define destination IP address and port
dest_ip = 'destination_ip_address'
dest_port = 12345  # Example destination port

# Define message to send
message = b'Hello, world!'  # Convert string to bytes

# Send UDP packet
udp_sock.sendto(message, (dest_ip, dest_port))

# Close socket when done
udp_sock.close()
