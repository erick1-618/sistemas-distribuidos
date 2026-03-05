import socket
from threading import Thread
from random import choice

def reqJob(t_name, conn):
    data = conn.recv(1024)
    conn.sendall(f'Sinal recebido pela Thread {t_name}: {data.decode()}'.encode())
    conn.close()

server = socket.socket()

server.bind(('localhost', 5000))

server.listen()

while True:
    conn, addr = server.accept()

    # Inicializando as threads que irão responder as requisições
    t1 = Thread(target=reqJob, name='T1', args=('T1', conn))
    t2 = Thread(target=reqJob, name='T2', args=('T2', conn))
    t3 = Thread(target=reqJob, name='T3', args=('T3', conn))

    thread_pool = (t1, t2, t3)

    t_selected = choice(thread_pool)

    t_selected.start()