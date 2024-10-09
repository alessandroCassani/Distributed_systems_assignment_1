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
        message_counter = random.randint(2,4)
        s.connect((SERVER_ADDRESS,SERVER_PORT))
        print(f'client connected!') 
        
        for i in range(message_counter):
            message = f'message number {i}'
            s.sendall(message.encode())
            print(f'message {i} sent')
            
            server_response = s.recv(1024).decode()
            print(f'received server response: {server_response}')
        
        sleeping_time = random.randint(1,5)
        print(f'sleeping for {sleeping_time} seconds...')
        time.sleep(sleeping_time)
        
        s.sendall(END_MESSAGE.encode())
        print('closing!')
        
       
if __name__ == '__main__':
    main()