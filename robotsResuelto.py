import threading
import random
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

tam = 10
cadena = []

coloco = threading.Semaphore(tam)
puedo_empaquetar = [threading.Semaphore(0), threading.Semaphore(0), threading.Semaphore(0)]
mutex = threading.Lock()

empaquetados = 0

class Colocador(threading.Thread):
    def __init__(self):
        global cadena, tam
        super().__init__()
        cadena = [0 for _ in range(tam)]

    def run(self):
        logging.info(f'Arranca Colocador ')
        while True:
            tipo = random.randint(0,2) + 1
            logging.info(f'Produciendo tipo {tipo}')
            time.sleep(random.randint(0,1))
            coloco.acquire()
            cero = cadena.index(0)
            cadena[cero] = tipo
            logging.info(f'Coloco un producto {tipo}')
            puedo_empaquetar[tipo-1].release()
            logging.info(f'Lista {cadena} ')


class Empaquetador(threading.Thread):
    def __init__(self, tipo):
        super().__init__()
        self.tipo = tipo

    def run(self):
        global empaquetados
        logging.info(f'Arranca Empaquetador {self.tipo}')
        while True:
            puedo_empaquetar[self.tipo - 1].acquire()
            indice = cadena.index(self.tipo)
            logging.info(f'Robot de tipo {self.tipo} empaquetando producto en posición {indice}')
            cadena[indice] = 0
            coloco.release()
            time.sleep(2)
            mutex.acquire()
            empaquetados += 1
            logging.info(f'Aumenta el número de empaquetados: {empaquetados}')
            mutex.release()

def main():
    empaquetador1 = Empaquetador(1)
    empaquetador2 = Empaquetador(2)
    empaquetador3 = Empaquetador(3)
    colocador = Colocador()

    colocador.start()
    empaquetador1.start()
    empaquetador2.start()
    empaquetador3.start()


if __name__ == '__main__':
    main()
