import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 8080

def main():
    create_client()
    

def create_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_ADDRESS,SERVER_PORT))
        
        print('client connected!')
        message = input('Insert the message to send to the server \n')
        
        s.sendall(message.encode())
        print('message sent!')
        
        data = s.recv(1024).decode()
        print(f'response received from the server: {data}')
    
    print('Connection closed')
    
    
if __name__ == '__main__':
    main()