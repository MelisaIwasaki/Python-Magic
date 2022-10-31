'''
Implemente un programa que lea el diametro D de un circulo e imprima:
a)El radio R del circulo(la mitad del diametro)
b)El area del circulo.Para calcular el area del circulo debe utilizar la formula PI*R^2
c)El perimetro del circulo.Debe utilizar la formula D*PI(o tambien PI*R*2)

'''
import constant
import random

pi_constante = (constant.PI)
diametro = float(random.randrange(20))
dos = 2
radio = diametro / dos 
area = (constant.PI *(radio * radio))
perimetro = (constant.PI * radio * dos)

print("Radio:")
print(round(radio))
print("Area:")
print(round(area))
print("Perimetro:")
print(round(perimetro))
