import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen()

clients = []

def broadcast(message, client):
    for c in clients:
        if c != client:
            c.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break

def receive():
    print("Server started...")
    while True:
        client, addr = server.accept()
        print(f"Connected with {addr}")
        clients.append(client)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()