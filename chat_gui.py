import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

window = tk.Tk()
window.title("Chat App 💬")

chat_area = scrolledtext.ScrolledText(window)
chat_area.pack(padx=10, pady=10)
chat_area.config(state='disabled')

msg_entry = tk.Entry(window, width=50)
msg_entry.pack(padx=10, pady=10)

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            chat_area.config(state='normal')
            chat_area.insert(tk.END, message + "\n")
            chat_area.config(state='disabled')
        except:
            break

def send():
    message = msg_entry.get()
    client.send(message.encode())
    msg_entry.delete(0, tk.END)

send_button = tk.Button(window, text="Send", command=send)
send_button.pack()

threading.Thread(target=receive).start()

window.mainloop()