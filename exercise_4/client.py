import threading
import socket
import random
import time

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 8080
END_MESSAGE = 'end'
    
def main():
    create_client()
            
def create_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_ADDRESS,SERVER_PORT))
        print(f'client connected!') 
        
        while(True):
            message = input("insert message to send to the server, otherwhise send 'end' string \n")
            s.sendall(message.encode())
            
            if message.lower() == END_MESSAGE:
                break
            
            server_response = s.recv(1024).decode()
            print(f'received server response: {server_response}')

        print('closing!')
        
       
if __name__ == '__main__':
    main()