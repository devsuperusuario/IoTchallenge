#Importar las bibliotecas necesarias

import numpy as np # Proporciona funciones y estructuras de datos para cálculos numéricos eficientes
import time # Provee funciones para trabajar con el tiempo que se usarán a lo largo del programa
from Adafruit_IO import Client # Importar las clases necesarias de la biblioteca Adafruit_IO
from Adafruit_IO import * # Importar las clases necesarias de la biblioteca Adafruit_IO



# Inicialización de un cliente de API REST en Adafruit IO utilizando [username] y [API Key]
aio = Client('superusuario', 'aio_uttU65PLgsIAjBlT1ih4FooYfuON')


# Se crea un objeto feed de nombre 'sinusoidal'
feed = Feed(name='sinusoidal')
# Se manda el objeto feed a Adrafruit Io para inicializar un FEED
result=aio.create_feed(feed)


# GENERADOR DE SEÑAL SINUSOIDAL

fs = 50e3           # Frecuencia de muestreo
f = 1000            # Representa de frecuencia de la señal sinusoidal
nCyl = 5            # Número de ciclos de la señal sinusoidal que se generarán
interval = 1 / fs   # Intervalo de tiempo entre muestras

t = 0

data = [] #Lista vacia para almacenar los datos generados y enviarlos a Adafruit
#datatime = []

while t < nCyl * 1/f:

    x = np.sin(2 * np.pi * f * t)   # Genera un punto de la señal sinosoidal

    data.append(x)                  # Agrega el dato a la lista 'data'
    t += interval                   # 
    #datatime.append(interval)
    time.sleep(interval)            # Tiempo de espera antes de la siguiente iteración

print("Ha comenzado el envío de datos con éxito")    
print(len(data))

# Enviar los datos generdos al feed 'sinusoidal' de Adafruit IO 

for x in range(len(data)):
    aio.send('sinusoidal', data[x])
    time.sleep(7.2)


print("Los datos han sido cargados exitosamente.")
time.sleep(2)
print("La onda sinusoidal ha sido generada en Adafruit.io")
time.sleep(2)
print("La ejecución de este programa duró 1836(seg) ---> 30.6 (min)")
time.sleep(2)
print("Este programa se autodestruirá en 5 seg")
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1.9)
print(r"""
                             ____
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")

""")
time.sleep(2)
print("Por: César Hernández-Ubaldo")





