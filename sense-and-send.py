# A simple Ultrasonic measure with UDP send using PicoPi W and HC-SR04 sensor
# See readme for details

# Import required components
from machine import Pin
import utime
import network
import socket as socket

# Define your pins
trigger = Pin(14, Pin.OUT) # Replace with your pin
echo = Pin(15, Pin.IN) # Replace with your pin

# Create function to measure distance
def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print("The distance from object is ",distance,"cm")
    return distance

# Connect to Wi-Fi
wifi = network.WLAN(network.STA_IF)  # STA_IF for station mode (client)
wifi.active(True)
wifi.connect('x', 'y')  # Replace 'SSID' and 'password' with your Wi-Fi credentials

# Wait until connected
while not wifi.isconnected():
    pass

# Print WiFi status to console
print('Connected to Wi-Fi:', wifi.ifconfig())

# Create UDP socket
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define destination IP address and port
dest_ip = 'a' # Replace with your IP
dest_port = b  # # Replace with your UDP port

# Define message to send
message = b'Connected!'  # Convert string to bytes

# Send UDP packet
udp_sock.sendto(message, (dest_ip, dest_port))

# Run main loop
while True:
    result = ultra()
    message = bytes(str(result),'utf-8')
    print(message)
    udp_sock.sendto(message, (dest_ip, dest_port))
    utime.sleep(1)

# Close socket when done (probably wont ever run anyway)
udp_sock.close()
