import threading
import socket
import random

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 8080
    
def main():
    create_client_threads()
    
    
    
def create_client_threads(n):
    threads = []
    for i in range(n):
        thread = threading.Thread(target=connect)
        thread.start()
        threads.append(thread)
        
        

def connect():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_ADDRESS,SERVER_PORT))
        print(f' thread {threading.current_thread.name()} connected!') 
        
        s.sendall(f'message sent from client {threading.current_thread.name()}')
    
    
if __name__ == '__main__':
    main()