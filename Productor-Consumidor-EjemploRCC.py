import threading
import logging
import random
import time

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

class Recurso():
    def __init__(self):
        self.mutex = threading.Semaphore(1)
        self.wait = threading.Semaphore(0)

class listaRecurso(Recurso):
    elementos = []
    maxElementos = 10

recurso1 = listaRecurso()


def regionCriticaProductor():
    with recurso1.mutex:
        while not len(recurso1.elementos) < recurso1.maxElementos:
            recurso1.wait.acquire()
        recurso1.elementos.append(random.randint(0,100))
        recurso1.wait.release()
        logging.info(f'Hay {len(recurso1.elementos)} elementos, : {recurso1.elementos}')


def regionCriticaConsumidor():
    with recurso1.mutex:
        while not len(recurso1.elementos) > 0:
            recurso1.wait.acquire()
        logging.info(f'Retiro el elemento {recurso1.elementos.pop(0)}, longitud de lista {len(recurso1.elementos)}')
        recurso1.wait.release()


def Productor():
    while True:
        regionCriticaProductor()
        time.sleep(random.randint(1,2))

def Consumidor():
    while True:
        regionCriticaConsumidor()
        time.sleep(random.randint(1,5))


threading.Thread(target=Productor, daemon=True).start()
threading.Thread(target=Consumidor, daemon=True).start()

time.sleep(300)