import threading
import time

# Tamanho do buffer
n = 5

mutex = threading.Semaphore(1)
empty = threading.Semaphore(n)
full = threading.Semaphore(0)

class Produtor(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def run(self):
        while True:
            time.sleep(1)
            
            empty.acquire()
            mutex.acquire()
            
            print(f'{self.name} produzindo')
            
            mutex.release()
            full.release()

class Consumidor(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def run(self):
        while True:
            time.sleep(1)
            
            full.acquire()
            mutex.acquire()
            
            print(f'{self.name} consumindo')
            
            mutex.release()
            empty.release()

def main():
    produtores = [Produtor(f'Produtor-{i}') for i in range(3)]
    consumidores = [Consumidor(f'Consumidor-{i}') for i in range(3)]

    for p in produtores:
        p.start()

    for c in consumidores:
        c.start()

if __name__ == "__main__":
    main()