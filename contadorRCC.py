import threading
import random
import time
import logging
import queue

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


class recursoInt():
    def __init__(self, valor_inicial=0):
        self.valorInt = valor_inicial
        self.lock = threading.Lock()


class Contador(threading.Thread):
    def __init__(self, recursoInt):
        super().__init__()
        self.recurso = recursoInt

    def RegionCritica1(self):
        with self.recurso.lock:
            self.recurso.valorInt += 1

    def run(self):
        for i in range(1000000):
            self.RegionCritica1()

variable = recursoInt()

hilos = []

for i in range(12):
    hilo = Contador(variable)
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

logging.info(f'Valor final = {variable.valorInt}')
