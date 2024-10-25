import socket

target_host = "127.0.0.1"
target_port = 9997
req_data = b"AAABBBCCC"

# Creating a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Sending some data to the server
client.sendto(req_data, (target_host, target_port))
print(f"Sent data to {target_host}:{target_port}")

# Receiving some data and source address(addr) i.e. server address
data, addr = client.recvfrom(4096)
    

# close socket
print(data.decode())
client.close()