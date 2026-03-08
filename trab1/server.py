import socket
from threading import Thread
from random import choice

class ReqJob(Thread):
    def __init__(self, t_name):
        super().__init__(name=t_name)
        self.t_name = t_name

    def start(self, conn):
        data = conn.recv(1024)
        conn.sendall(f'Sinal recebido por {self.t_name}: {data.decode()}'.encode())
        conn.close()

# Inicializando as threads
thread_pool = [ReqJob('Thread-1'), ReqJob('Thread-2'), ReqJob('Thread-3'), ReqJob('Thread-4'), ReqJob('Thread-5')]

server = socket.socket()

server.bind(('localhost', 5000))

server.listen()

while True:
    conn, addr = server.accept()

    t_selected = choice(thread_pool)

    t_selected.start(conn)