import threading
import random
import time
import logging
import queue

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


class BufferMonitor():
    def __init__(self, capacidad):
        super().__init__()
        self.buffer = []
        self.capacidad = capacidad
        self.primero = 0
        self.ultimo = 0
        self.cuenta = 0
        self.lock = threading.RLock()
        self.nolleno = threading.Condition(self.lock)
        self.novacio = threading.Condition(self.lock)

    def insertar(self, dato):
        with self.lock:
            while (self.cuenta == self.capacidad):
                self.nolleno.wait()
            self.buffer.insert(self.ultimo, dato)
            self.ultimo = (self.ultimo+1) % self.capacidad
            self.cuenta += 1
            self.novacio.notify_all()

    def extraer(self):
        with self.lock:
            while (self.cuenta == 0):
                self.novacio.wait()
            resultado = self.buffer[self.primero]
            self.primero = (self.primero + 1) % self.capacidad
            self.cuenta -= 1
            self.nolleno.notify_all()
            return resultado

class HiloProductor(threading.Thread):
    def __init__(self, bufferMon):
        super().__init__()
        self.buffer = bufferMon

    def run(self):
        while True:
            valor = random.randint(0,99)
            self.buffer.insertar(valor)
            logging.info(f'Hilo {threading.current_thread().name} produjo el dato {valor} ')
            time.sleep(2)

class HiloConsumidor(threading.Thread):
    def __init__(self, bufferMon):
        super().__init__()
        self.buffer = bufferMon


    def run(self):
        while True:
            valor = self.buffer.extraer()
            logging.info(f'Hilo {threading.current_thread().name} consumio dato = {valor} ')
            time.sleep(3)

bufferMon = BufferMonitor(5)
hilos = []

for i in range(10):
    hilo = HiloConsumidor(bufferMon)
    hilo.start()
    hilos.append(hilo)
    hilo = HiloProductor(bufferMon)
    hilo.start()
    hilos.append(hilo)


