import socket

# Create a client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(("127.0.0.1", 5000))

print("Connected to DNS Server")

while True:
    # Ask user for a domain name
    domain = input("Enter domain name: ")

    # Send domain name to server
    client.send(domain.encode())

    if domain.lower() == "exit":
        break

    # Receive result from server
    result = client.recv(1024).decode()

    print(result)

# Close connection
client.close()