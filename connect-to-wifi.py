# Simple connect to WiFi example for the Pico Pi W
import network

# Connect to Wi-Fi
wifi = network.WLAN(network.STA_IF)  # STA_IF for station mode (client)
wifi.active(True)
wifi.connect('SSID', 'password')  # Replace 'SSID' and 'password' with your Wi-Fi credentials

# Wait until connected
while not wifi.isconnected():
    pass

print('Connected to Wi-Fi:', wifi.ifconfig())
