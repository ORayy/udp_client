# udp_client

        UDP CLIENT                                  SERVER
   .-----------------.                      .-------------------.
   |                 |                      |                   |
   |  Send Request   |--------------------->|  Await Request    |
   |   "Hello!"      |                      |                   |
   |                 |                      |                   |
   |                 |                      |                   |
   |   UDP Socket    |<---------------------|  Send Response    |
   |  Receive Data   |                      |    "Hi, Client!"  |
   |                 |                      |                   |
   '-----------------'                      '-------------------'

         |                                                |
         |<------------ Connectionless Protocol ---------->|

        Communication happens over UDP with no setup
        or teardown of a connection, meaning faster,
          more lightweight messages than with TCP.



# Simple UDP Client in Python

This Python script implements a basic UDP client that sends data to a specified server and waits for a response. It demonstrates a fundamental approach to using the User Datagram Protocol (UDP) for client-server communication in Python.

## Prerequisites

- **Python 3.x**: Make sure you have Python installed on your system.
- **Network Access**: Ensure that the target server is accessible and that there’s a service listening on the target IP address and port.

## How It Works

- The client creates a UDP socket using Python’s `socket` library.
- The specified data is sent to the target IP address and port.
- The client then waits for a response from the server, displaying it if received.
- Finally, the client closes the socket connection.

## Code Overview

""" python
import socket

target_host = "127.0.0.1"  # IP of the server
target_port = 9997          # Port on the server
req_data = b"AAABBBCCC"     # Data to be sent

# Creating a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Sending data to the server
client.sendto(req_data, (target_host, target_port))
print(f"Sent data to {target_host}:{target_port}")

# Receiving a response from the server
data, addr = client.recvfrom(4096)
print(data.decode())

# Close the socket
client.close()
"""

Usage
1) Run the Server: Make sure a UDP server is running on the target host and port.

2) Run the Client: Execute the following command to run the client:
python udp_client.py

3) Output: If a response is received from the server, it will be displayed in the console.

Example Output:
Sent data to 127.0.0.1:9997
Response from server: Hello, UDP Client!

+++ Important Notes +++
This client uses a non-blocking approach, so make sure a server is actively listening on the specified IP and port.
The recvfrom function waits indefinitely for a response; you may add a timeout if needed.
License
This project is licensed under the MIT License. See LICENSE for details.

Happy Hacking!