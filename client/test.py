from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time

# GLOBAL CONSTANTS
HOST = "localhost"
PORT = 5500
ADDR = (HOST, PORT)

# GLOBAL VARIABES
messages = []
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
BUFSIZ = 512


def receive_messages():
    """receive messages from server
    : return home
    """
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode()
            messages.append(msg)
            print(msg)
        except Exception as e:
            print("[EXCEPTION]", e)


def send_message(msg):
    """send messages to the server

    Args:
        msg (str):
    """
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()


receive_thread = Thread(target=receive_messages)
receive_thread.start()

send_message("The World")
time.sleep(3)
send_message("you are a god and we all know that...")
