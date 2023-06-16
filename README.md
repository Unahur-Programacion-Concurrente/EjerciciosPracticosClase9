# Semaforos

## Ejercicio 1 - Vaquitas
````
vaquitas.py
`````
Vamos a simular que hay vacas yendo por un camino, todas para el mismo lado, y se topan con un puente.
Las vacas caminan a diferentes velocidades, y el puente no soporta el paso de más de una vaca a la vez.

Mirá la implementación que esta ahora, correla algunas veces, y familiarizate con el código.

Ahora agregale semáforos para asegurar que haya solamente una vaca cruzando el puente a la vez. La ejecución debería verse así:

![vaquitas cruzando el puente](assets/vaquitas.gif)

## Ejercicio 2 - Robots
````
robots.py
`````
En una cadena de montaje existe un robot encargado de colocar productos de 3 tipos diferentes (1, 2 o 3) en la cadena de montaje.

Otros robots, retiran los productos de la cadena de montaje para realizar su empaquetado, teniendo en cuenta que están especializados en un solo tipo de producto (1, 2 o 3), ignorando los que no son de su tipo.

Finalmente, se quiere llevar un control del total de productos empaquetados (independientemente de su tipo).

Modelar utilizando semáforos el sistema descrito con las siguientes indicaciones:


- Modelar cada robot como un hilo (1 colocador y 3 empaquetadores, uno para cada tipo de producto).


- Los productos son colocados de uno en uno en la cadena, y solamente en posiciones libres (se puede considerar que en la cadena de montaje caben un máximo N de elementos).


- Si no hay posiciones libres el robot colocador tendrá que esperar hasta que algún producto sea retirado de la cadena.


- Los robots empaquetadores se especializan en un tipo de producto (1, 2 o 3) en tiempo de inicialización.


- Los robots empaquetadores comprueban si hay algún elemento de su tipo en la cadena ignorando los productos que no sean de su tipo. Si hay algún producto de su tipo lo retiran de la cadena (sólo 1 producto cada vez) y la posición queda libre para colocar nuevos productos, en caso contrario se quedan a la espera de que haya nuevos productos.


- Los robots empaquetadores de distinto tipo pueden funcionar a la vez.

- Tanto el colocador como los empaquetadores ejecutan un bucle infinito (no terminan)

- Cada vez que un robot empaquetador procesa un producto, la cuenta total de productos empaquetados debe aumentar y mostrarse un mensaje por pantalla.

## Ejercicio 3 - Productor - Consumidor
````
Ejemplo1.py
`````
El siguiente programa implementa un hilo productor y N hilos consumidores (N = 5) todos compartiendo un objeto "cola" sincronizada (queue.Queue):

- El hilo productor ejecuta un bucle infinito donde inserta un valor entero aleatorio (entre 1 y 5) en la cola y luego espera un tiempo aleatorio (0 o 1 segundo) antes de la siguiente iteración.

- Los hilos consumidores ejecutan un bucle infinito donde toman N valores de la cola (no tienen que ser consecutivos), los almacena en una lista local. 
  

- Cada hilo toma los valores de a uno sin bloquear a otros hilos entre toma y toma.
  

- Finalmente imprime un mensaje con la lista y el promedio de los valores de la misma y espera un tiempo aleatorio antes de la siguiente iteración.

### Ejercicios

1. Utilizando SEMAFOROS, modificar el código de modo que en todo momento la cantidad de hilos consumidores tomando datos de la cola no sean mas que 2. 

2. Resolver el ejercicio anterior utilizando variables de condición.

3. Como implementaria una condición con semáforos?

# Regiones Críticas Condicionales

### Ejercicio 

Resolver el ejercicio anterior implementando Regiones Críticas Condicionales