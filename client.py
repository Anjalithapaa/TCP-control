import socket

def run_client():
    server_name = 'localhost'
    server_port = 8008

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_name, server_port))

    commands = ["HELO W0725561",
                "REQTIME",
                "REQDATE",
                "ECHO 329 is fun.",
                "REQIP",
                "BYE"]

    for command in commands:
        client_socket.send(command.encode())
        response = client_socket.recv(1024).decode()
        print("Client sent: {}\nFrom Server: {}\n".format(command, response))

    client_socket.close()

if __name__ == "__main__":
    run_client()
