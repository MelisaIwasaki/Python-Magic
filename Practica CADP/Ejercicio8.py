"""
Realice un programa que informe el valor total en dolares de una transaccion en 
dolares.Para ello el programa debe leer el monto total en dolares de la transaccion,
el valor de dolar al dia de la fecha y el porcentaje(en pesos)de la comision que 
cobra el banco con la transaccion.Por ejemplo si la transaccion se realiza por 10 
dolares,el dolar tiene un valor 20.54 pesos y el banco cobra un 4% de comision,
entonces el programa debera informar:'La transaccion sera de 213.61 pesos argentinos'
resultado de multiplicar(10*20.54 y adicionarle 4%).

"""

import random

dolar = float(random.randrange(100))
valor = float(random.randrange(100))
comision = float(random.randrange(100))

pesos = dolar * valor
transaccion = pesos + (pesos* comision/100)
print("Valor de la transaccion")
print(round(transaccion))
