"""

Realizar un programa que lea dos numeros enteros desde el teclado e informe en pantalla 
cual de los dos numeros es el mayor.Si son iguales se debe informar en pantalla lo siguiente:
"Los numeros leidos son iguales"

"""

import random

numero1 = int(random.randrange(100))
numero2 = int(random.randrange(100))

if numero1 > numero2 :
    print("El primero es mayor que el segundo")
if numero1 == numero2 :
    print("Los dos numeros son iguales")
    
