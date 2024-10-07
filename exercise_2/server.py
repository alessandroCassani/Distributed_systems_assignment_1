import socket
from sys import argv

HOST = "0.0.0.0"
DEFAULT_PORT = 8080

def main():
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
            print('new connection established!')
        
            data = conn.recv(1024).decode()
            print(f'data received Client {addr}: {data}')
            
            conn.sendall('server response'.encode())
            print('server response sent')
        
        print('connection closed')
    
    
if __name__ == "__main__":
    main()
