import socket
import threading
import json

id = int(input("ID do processo (0, 1 ou 2): "))
peers = [("localhost", 5000), ("localhost", 5001), ("localhost", 5002)]

clock = 0
queue = []
acks = {}

lock = threading.Lock()

def broadcast(msg):
    for host, port in peers:
        try:
            s = socket.socket()
            s.connect((host, port))
            s.send(json.dumps(msg).encode())
            s.close()
        except:
            pass


def send_message(content):
    global clock

    with lock:
        clock += 1
        ts = clock

    msg = {
        "type": "MSG",
        "timestamp": ts,
        "sender": id,
        "content": content
    }

    queue.append(msg)
    acks[(ts, id)] = set([id])

    broadcast(msg)


def handle_message(msg):
    global clock

    with lock:
        clock = max(clock, msg["timestamp"]) + 1

    if msg["type"] == "MSG":
        queue.append(msg)

        ack = {
            "type": "ACK",
            "timestamp": msg["timestamp"],
            "sender": msg["sender"],
            "from": id
        }

        broadcast(ack)

    elif msg["type"] == "ACK":
        key = (msg["timestamp"], msg["sender"])

        if key not in acks:
            acks[key] = set()

        acks[key].add(msg["from"])

    deliver()


def deliver():
    queue.sort(key=lambda x: (x["timestamp"], x["sender"]))

    while queue:
        msg = queue[0]
        key = (msg["timestamp"], msg["sender"])

        if key in acks and len(acks[key]) == len(peers):
            print(f"[Processo {id}] Entregue: {msg['content']}")
            queue.pop(0)
        else:
            break


def server(port):
    s = socket.socket()
    s.bind(("localhost", port))
    s.listen()

    while True:
        conn, _ = s.accept()
        data = conn.recv(1024)

        if data:
            msg = json.loads(data.decode())
            handle_message(msg)

        conn.close()


threading.Thread(target=server, args=(peers[id][1],), daemon=True).start()

while True:
    text = input("Mensagem: ")
    send_message(text)