import socket

while True:

    client = socket.socket()
    
    client.connect(('localhost', 5000))
    
    req = input('Digita o que irá enviar:')
    
    client.sendall(req.encode())

    res = client.recv(1024)

    print(f'Resposta do servidor: {res.decode()}')