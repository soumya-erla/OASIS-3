import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("Error!")
            client.close()
            break

def write():
    while True:
        message = input("")
        client.send(message.encode())

threading.Thread(target=receive).start()
threading.Thread(target=write).start()