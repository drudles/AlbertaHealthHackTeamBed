#  Imports:
import socket  # Used for the communication
import threading  # Used to run stuff in the background

HOST = "10.0.0.116"
PORT = 1234  # You can use any port between 0 to 65535
LISTENER_LIMIT = 2
active_users = []  # a list of all currently connected users

# This function will listen for any upcoming messages from a client
def listen_for_messages(client, username):

    while 1:
        message = client.recv(2048).decode('utf-8')
        if message != '':
            final_msg = username + ": " + message
            send_messages(message=final_msg)
        else:
            print('The Message Sent From Client ' + username + ' is Empty')

# Function to send a message to a specific person
def send_message_to_client(client, message):

    client.sendall(message.encode())

# Function to send any new message to all clients in chat room
def send_messages(message):

    for user in active_users:
        send_message_to_client(user[1], message)

# Function to handle client
def client_handler(client):

    # Server will listen for client message that will contain the username
    while 1:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_users.append((username, client))
            prompt_message = "SERVER~" + f"{username} added to the chat"
            send_messages_to_all(prompt_message)
            break
        else:
            print("Invalid Username!")

    threading.Thread(target=listen_for_messages, args=(client, username)).start()

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

    # Set Server limit for how many users can join a chat room at a time
    server.listen(LISTENER_LIMIT)

    # This while loop will keep listening to client connections
    while 1:

        client, adress = server.accept()
        print("Successfully Connected to Client " + str(adress[0]) + " " + str(adress[1]))

        threading.Thread(target=client_handler, args=(client, )).start()
        

if __name__ == '__main__':
    main()
