import socket



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_Inet is the family ipv4
# socket.sockstream is the network protocol (TCP)

host = socket.gethostname()

port = 8080

client_socket.connect((host, port))

message = client_socket.recv(1024)


client_socket.close()


print(message.decode("ascii"))