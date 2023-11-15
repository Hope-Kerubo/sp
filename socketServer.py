import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

"""
with- used to wrap the execution of a block with methods defined by a context manager.
socket() - returns a socket object whose methods implement the various socket system calls.
aruments passed in socket() are constants used to specify the address family and socket type.
AF_INET is the Internet address family for IPv4. 
SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport messages in the network.
values passed to .bind depend on the address family of the socket. 
In this case, were using ipv4 so it expects to records, a host and a port.

"""