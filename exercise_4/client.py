import threading
import socket
import random
import time

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 8080
END_MESSAGE = 'end'
    
def main():
    n = input('select the number of clients to launch \n')
    create_client_threads(int(n))
    
    
    
def create_client_threads(n):
    for i in range(n):
        thread = threading.Thread(target=connect)
        thread.start()
        
        
def connect():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_ADDRESS,SERVER_PORT))
        print(f'{threading.current_thread().name} connected!') 
        
        message = f'message sent from client {threading.current_thread().name}'
        s.sendall(message.encode())
        
        server_response = s.recv(1024).decode()
        print(f'server response received: {server_response}')
        
        sleeping_time = random.randint(1,6)
        time.sleep(sleeping_time)
        
        s.sendall(END_MESSAGE.encode())
        
    
    
if __name__ == '__main__':
    main()