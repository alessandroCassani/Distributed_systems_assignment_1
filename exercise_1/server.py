import socket
from sys import argv

def main():
    HOST = "0.0.0.0"
    DEFAULT_PORT = 8080
    
    try:
        port = int(argv[1])
    except:
        port = DEFAULT_PORT

    print(f"Server started on port {port}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, port))
        s.listen()
        
        print("Waiting for a client...")
        conn, addr = s.accept()
        
        with conn:  
            print('New connection established!')
            data = conn.recv(1024).decode()
            print(f'Data received from client {addr}: {data}')
        
        print('Connection closed')
    

if __name__ == "__main__":
    main()
