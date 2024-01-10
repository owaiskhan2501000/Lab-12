import socket

def connect_to_server(server_address, port):
    try:
        with socket.create_connection((server_address, port), timeout=5) as sock:
            print(f"Connected to {server_address}:{port}")
    except ConnectionError as ce:
        print(f"ConnectionError: Could not establish a connection to {server_address}:{port}")
    except socket.error as se:
        print(f"SocketError: {se}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

server_address = "example.com"
port = 80

connect_to_server(server_address, port)
