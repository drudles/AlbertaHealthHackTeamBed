# Imports:
import socket
import threading

HOST = "127.0.0.1"
PORT = 1234

def main():

    # Creating a socket client
    # AF_INET means we are going to use IPv4 Adresses
    # SOCK_STREAM means we are using TCP packets for communication
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the Server
    try:
        client.connect((HOST, PORT))
        print("Succressfully Connected to Server!")
    except:
        print("Unable to Connect to Server: " + HOST + " " + str(PORT))

if __name__ == '__main__':
    main()
