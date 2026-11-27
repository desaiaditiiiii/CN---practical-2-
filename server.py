import socket

# Create a server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Give the server an address and port
server.bind(("127.0.0.1", 5000))

# Wait for a client
server.listen(1)

print("DNS Server is running...")

# Accept client connection
conn, addr = server.accept()

print("Client connected")

while True:
    # Receive domain name from client
    domain = conn.recv(1024).decode()

    if not domain or domain.lower() == "exit":
        break

    try:
        # Find the IP address
        ip = socket.gethostbyname(domain)
        result = "IP Address: " + ip

    except socket.gaierror:
        result = "Domain not found"

    # Send IP address to client
    conn.send(result.encode())

# Close connection
conn.close()
server.close()