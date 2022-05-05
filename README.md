# SSL Communication using Sockets in Python
## Network Security Project AY 2022
## Authors
 [Chandan]()
 
 [Harshad_Dhane]()
 
 [Avinash_Reddy]()

###Problem
> Two-way authenticated SSL communication

###Approach
>Back in mid 90's the beginning of the Internet era, very little part of the internet was encrypted because there were only few people on the internet at that time and fewer credit card details shared online.But as the internet grew in popularity new industries emerged such as online shopping and online banking which required data to be encrypted to keep it safe from intruders and made sure access was provided to authentic users only.That was when HTTPS was developed with the help of SSL .Which sits above transport layer and below  application layer.
###Algorithm
><a href="https://msatechnosoft.in/blog/wp-content/uploads/2017/06/SSL-flowchart-msa-technosoft.png"/>

### Algorithm 

#### Obtaining Certificate
- Using pyopenssl & urllib you can mention a valid https website
- After which ssl.get_server_certificate((addr, port), ssl_version=3) obtains the certificate where ssl_version mentions the version of ssl being used
- Then using crypto.load_certificate(crypto.FILETYPE_PEM, cert) we get the X.509 certificate


#### Sockets communication
<h3>Server side</h3>
- Using sockets we establish a communication 
- server_ssl=ssl.wrap_socket(clientsocket,server_side=True,certfile="certificate.pem",keyfile="key.pem",ssl_version=ssl.PROTOCOL_TLSv1)
- In the above line we wrap the communcation in SSL where clientsocket is the new thread to handle that communication and server_side is set to True to let the SSL library know this is server side , certfile contains the location of the certifcate , keyfile contains the location of the private key of the server and ssl_version mentions the version of ssl being used. 
- When the server recieves the message from client then SSL.read() is used to read the message
- print(server_ssl.cipher()) Returns the version of encryption being used in this SSL
<h3>Client side</h3>
  - We use client_ssl=ssl.wrap_socket(socket_obj,ca_certs="certificate.pem") to wrap the socket in SSL and mention the server certificate we recieved.
  - We use client_ssl.write(message.encode()) to encrypt the message and send the message 

Output:
<a href="Capture.PNG"/>
