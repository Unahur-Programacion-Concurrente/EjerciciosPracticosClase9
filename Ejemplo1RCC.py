import threading
import random
import time
import logging
import queue

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

sem1 = threading.Semaphore(0)
lock = threading.Lock()


#cola = queue.Queue(0)
valores = []

class recursoCola():
    def __init__(self, max_items, max_cons):
        self.cola = queue.Queue(max_items)
        self.num_max_cons = max_cons
        self.condicion = threading.Condition()


class productor(threading.Thread):
    def __init__(self, recurso):
        super().__init__()
        self.recurso = recurso

    def run(self):
        global valores
        while True:
            valor = random.randint(1,5)
            self.recurso.cola.put(valor)
            with lock:
                valores.append(valor)
            logging.info(f'Se produjo el valor {valor}, cola {valores}')
            #     logging.info(f'Se produjo el valor {valor}')
            #    logging.info(f'Se produjo el valor {valor}, cola {cola.queue}')
            time.sleep(random.randint(0,1))

class recursoCola():
    def __init__(self, max_items):
        self.cola = queue.Queue(max_items)
        self.num_max_cons = 0
        self.condicion = threading.Condition()

class consumidor(threading.Thread):
    def __init__(self, recurso, items_medida):
        super().__init__()
        self.medida = []
        self.recurso = recurso
        self.items_medida = items_medida

    def regionNumCons(self):
        with self.recurso.condicion:
            while self.recurso.num_max_cons == 2:
                self.recurso.condicion.wait()
            self.recurso.num_max_cons += 1
            for k in range (self.items_medida):
                item = self.recurso.cola.get()
                self.medida.append(item)
                time.sleep(random.randint(0,1))
                    #    logging.info(f'Consumió el valor {item}')
            self.recurso.num_max_cons  -= 1
            logging.info(f'medida {self.medida} promedio = {sum(self.medida) / len(self.medida)}')
            self.recurso.condicion.notify_all()

    def run(self):
        while True:
            self.medida.clear()
            self.regionNumCons()
            time.sleep(random.randint(0,1))


recurso = recursoCola(0)
hilos = []
for i in range(15):
    hilo = consumidor(recurso, random.randint(2,5))
    hilos.append(hilo)

hilo = productor(recurso)
hilos.append(hilo)

for hilo in hilos:
    hilo.start()



