
import socket
import ssl
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj.bind((socket.gethostname(), 1024))
socket_obj.listen(5)
print ("Server is ready")
clientsocket, address = socket_obj.accept()
print ("Got connection from", address )
server_ssl=ssl.wrap_socket(
    clientsocket,
    server_side=True,
    certfile="certificate.pem",
    keyfile="key.pem",
    ssl_version=ssl.PROTOCOL_TLSv1

)

try:

    while server_ssl:
        message=server_ssl.read()
        if(message):
            print(message)
            print(server_ssl.cipher())
      
except Exception as ex:
    server_ssl.close()
    clientsocket.close()
