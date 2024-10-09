import threading
import socket
from sys import argv

HOST = "0.0.0.0"
DEFAULT_PORT = 8080
END_MESSAGE = 'end'

def main():
    try:
        port = int(argv[1])
    except:
        port = DEFAULT_PORT
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,port))
        s.listen()
        print(f'server listening on port {port}... \n')
        
        while(True):
            conn, addr = s.accept()
            print(f"New connection from {addr}")
            
            thread = threading.Thread(target=handle_connection, args=(conn,addr))
            thread.start()
            
            
def handle_connection(conn,addr):
    thread_name = threading.current_thread().name
    with conn:
        while True:
            data = conn.recv(1024).decode()
            print(f'server {thread_name} received following message from {addr}: {data}')

            if data == END_MESSAGE:
                print(f'server {thread_name} closing connection...')
                break
            else:
                response = f'response from server {thread_name}'
                conn.sendall(response.encode())
        

if __name__ == "__main__":
    main()