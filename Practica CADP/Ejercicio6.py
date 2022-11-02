"""
Un kiosquero debe vender una cantidad x de caramelos entre y clientes,dividiendo cantidades 
iguales entre todos los clientes. Los que sobren se los quedara para el.
a)Realice un programa que lea la cantidad de caramelos que posee el kiosquero (x),la cantidad 
de clientes(y), e imprima en pantalla un mensaje informando la cantidad de caramelos que le 
correspondera a cada cliente, y la cantidad de caramelos que se quedara para si mismo.
b)Imprima en pantalla el dinero que debera cobrarel kiosquero si cada caramelo tiene un valor
de $1.60. 

"""
import constant
import random

CAR = (constant.caramelo)
kiosquero = float(random.randrange(100))
clientes = float(random.randrange(100))

cantidad = kiosquero / clientes
resto = cantidad % clientes
precio = cantidad * CAR

print(cantidad)
print(resto)
print(round(precio))
