import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# socket family ipv4 (socket.AF_INET)
# connection protocol (TCP) (socket.SOCK_STREAM)
# connection protocol (UDP) (socket.SOCK_DGRAM)

# storing the host name 

host = socket.gethostname()
port = 8080

# binding  sever socket with the host and the port
server_socket.bind((host, port))

# tcp listener

server_socket.listen(3) # how many request allowed at a given time


while True:
    clientsocket, address = server_socket.accept()

    print("Recieved connection from %s " % str(address))

    message = "Hello! Thank you for connecting to the server" + "\r\n"
    
    clientsocket.send(message.encode("ascii"))
    clientsocket.close() 