#W0725561
#Anjali Thapa
#cmps329

import socket
import time

def handle_client(client_socket):
    while True:
        command = client_socket.recv(1024).decode()
        if not command:
            break  

        print("Received command: ", command)

        if command.startswith("HELO"):
            client_name = command.split(" ", 1)[1]
            response = "Hello {}, pleased to meet you.".format(client_name)
        elif command == "REQTIME":
            response = time.strftime("%H:%M:%S", time.localtime())
        elif command == "REQDATE":
            response = time.strftime("%Y-%m-%d", time.localtime())
        elif command.startswith("ECHO"):
            text = command.split(" ", 1)[1]
            response = text
        elif command == "REQIP":
            client_address = client_socket.getpeername()[0]
            response = client_address
        elif command == "BYE":
            response = "See ya later W0725561!"
            client_socket.send(response.encode())
            client_socket.close()
            return  
        client_socket.send(response.encode())

def run_server():
    server_name= 'localhost'
    server_port = 8008  
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)

    print("The server W0725561 is ready to receive on port {}".format(server_port))

    while True:
        connection_socket, addr = server_socket.accept()
        print("Connection from {}".format(addr))
        handle_client(connection_socket)

if __name__ == "__main__":
    run_server()
