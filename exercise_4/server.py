import threading
import socket
from sys import argv



def main():
    HOST = "0.0.0.0"
    DEFAULT_PORT = 8080
    
    try:
        port = int(argv[1])
    except:
        port = DEFAULT_PORT
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(HOST,port)
        s.listen()
        
        while(True):
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_connection)
            thread.start()
            
            
    
def handle_connection(conn):
    while(True):
        data = conn.recv(1024).decode()
        print(f'thread {threading.current_thread.name()} received following message: {data}')

        if data == 'end':
            break
        else:
            conn.sendAll(f'response from  {threading.current_thread.name()}').encode()
        

if __name__ == "__main__":
    main()