import threading
import random
import time
import logging
import queue

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
#sem1 = threading.Semaphore(2)

cola = queue.Queue(0)

class productor(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global valores
        while True:
            valor = random.randint(1,5)
            cola.put(valor)
      #      logging.info(f'Se produjo el valor {valor}')
      #      logging.info(f'Se produjo el valor {valor}, cola {cola.queue}')
            time.sleep(random.randint(0,1))

class consumidor(threading.Thread):
    def __init__(self, items):
        super().__init__()
        self.medida = []
        self.items = items

    def run(self):
        while True:
            self.medida.clear()
            for k in range (self.items):
                item = cola.get()
                self.medida.append(item)
                time.sleep(random.randint(1,2))
            #    logging.info(f'Consumió el valor {item}')
            logging.info(f'medida {self.medida}, promedio = {sum(self.medida)/self.items}')

hilos = []
for i in range(5):
    hilo = consumidor(random.randint(2,5))
    hilos.append(hilo)

hilo = productor()
hilos.append(hilo)

for hilo in hilos:
    hilo.start()


