'''
Realizar un programa que lea dos numeros enteros desde el teclado e informe en pantalla cual 
de los dos numeros es el mayor.Si son iguales se debe informar en pantalla lo siguiente:
"Los numeros leidos son iguales"

'''
import random

num1 = int(random.randrange(10))
num2 = int(random.randrange(10))

if num1 == num2 :
    print("Los numeros ingresados son iguales")
else:
    print("Los numeros ingresados no son iguales")
