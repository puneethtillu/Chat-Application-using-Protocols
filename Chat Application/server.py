# chat_server.py

import socket
import threading

clients = []  # List to store connected clients

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            # Broadcast the message to all connected clients
            for client in clients:
                client.send(message.encode("utf-8"))
        except Exception as e:
            print(f"Error handling client: {e}")
            break

    client_socket.close()

def main():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Chat server listening on {host}:{port}")

    while True:
        client, addr = server_socket.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        clients.append(client)
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    main()
