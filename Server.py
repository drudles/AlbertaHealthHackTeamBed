#  Imports:

import socket  # Used for the communication
import threading  # Used to run stuff in the background

HOST = "127.0.0.1"
PORT = 1234  # You can use any port between 0 to 65535
LISTENER_LIMIT = 2

def main():
    # Creating server class object
    # AF_INET means we are going to use IPv4 Adresses
    # SOCK_STREAM means we are using TCP packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Creating a try catch block
    try:
        server.bind((HOST, PORT))  # Telling our server to bind to this host and port
        print("Running Server on " + HOST + " " + str(PORT))
    except:
        print("Failed to bind to Host: " + HOST + " and PORT: " + str(PORT))

    # Set Server limit
    server.listen(LISTENER_LIMIT)

    # This while loop will keep listening to client connections
    while 1:

        client, adress = server.accept()
        print("Successfully Connected to Client " + str(adress[0]) + " " + str(adress[1]))

if __name__ == '__main__':
    main()
