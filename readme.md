# Pico Pi W and the HC-SR04

This repository contains sample Python code files for using an ultrasonic sensor with a Pico Pi W and UDP communications.

## Prerequisites

The following items are required:

 - Pico Pi W (https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
 - HC-SR04 (https://www.sparkfun.com/products/15569)

## Usage

Follow the steps below to use the sample Python code:

1. **Cable to Pico Pi W and sensor**: Ensure your Pico Pi W and sensor are wired correctly (a simple tutorial can be found here https://www.tomshardware.com/how-to/raspberry-pi-pico-ultrasonic-sensor)

2. **Connect your Pico W**: Connect to your Pico Pi using an IDE (Thonny or VSCode with MicroPico extension).

3. **Grab the code**: Clone this repo in VSCode or copy paste the code into Thonny, the main code file for the Pico Pi W is sense-and-send.py

4. **Fix the code** Change the variables to suit your needs in the sense-and-recieve.py and udp-recieve.py (look for the "replace" comments) 

5. **Start a UDP server on your host**: Start a the UDP server script on your host:

    ```bash
    python udp-recieve.py
    ```
    This will execute the script and print the UDP messages to the console.

6. **Start the script on the Pico Pi W** Start the sense-and-send.py script on the Pico Pi W and watch for the results in the console and UDP output script. 

## Contributing

If you'd like to contribute to this sample code repository, feel free to fork the repository, make your changes, and submit a pull request. Contributions such as bug fixes, improvements, or additional features are welcome.
