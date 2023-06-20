import threading
import random
import time
import logging
import queue

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# Recurso

class variableEntera():
    def __init__(self, valor_inicial=0):
        self.valorEntero = valor_inicial
        self.lock = threading.Lock()

class MonitorContador():
    def __init__(self, variable):
        self.lock = variable.lock
        self.variable = variable

    def incrementar(self):
        with self.lock:
            self.variable.valorEntero += 1

    def getValor(self):
        with self.lock:
            return self.variable.valorEntero

class HiloContador(threading.Thread):
    def __init__(self, monitorContador):
        super().__init__()
        self.contador = monitorContador

    def run(self):
        for i in range(1000000):
            self.contador.incrementar()


variable = variableEntera()

contador = MonitorContador(variable)

hilos = []

for i in range(10):
    hilo = HiloContador(contador)
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

logging.info(f'Valor final = {contador.getValor()}')