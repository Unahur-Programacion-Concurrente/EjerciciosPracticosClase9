import threading
import random
import time
import logging
import queue

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

sem2 = threading.Semaphore(5)
sem1 = threading.Semaphore(2)
lock = threading.Lock()


cola = queue.Queue(10)
valores = []
class productor(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global valores
        while True:
            valor = random.randint(1,5)
            cola.put(valor)
            with lock:
                valores.append(valor)
       #     logging.info(f'Se produjo el valor {valor}, cola {valores}')
       #     logging.info(f'Se produjo el valor {valor}')
        #    logging.info(f'Se produjo el valor {valor}, cola {cola.queue}')
            time.sleep(random.randint(0,1))

class consumidor(threading.Thread):
    def __init__(self, items):
        super().__init__()
        self.medida = []
        self.items = items

    def run(self):
        while True:
            self.medida.clear()
            with sem1:
                for k in range (self.items):
                    item = cola.get()
                    self.medida.append(item)
                    time.sleep(random.randint(0,1))
            #    logging.info(f'Consumió el valor {item}')
                logging.info(f'medida {self.medida} promedio = {sum(self.medida)/self.items}')
            time.sleep(random.randint(0,1))

hilos = []
for i in range(15):
    hilo = consumidor(2)
    hilos.append(hilo)

hilo = productor()
hilos.append(hilo)

for hilo in hilos:
    hilo.start()


