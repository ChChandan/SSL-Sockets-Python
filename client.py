import socket
import ssl

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_ssl=ssl.wrap_socket(socket_obj,
ca_certs="certificate.pem")
client_ssl.connect((socket.gethostname(), 1024))

while True:
    message=input("Please enter your message:-")
    if(message):
        if(message=="exit"):
            break
        else:
            client_ssl.write(message.encode())
    

socket_obj.close()

