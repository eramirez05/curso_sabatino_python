#Pograma que calcula la edad de una persona conociendo el año actual y el año de nacimineto
#Entrada
from math import sqrt

año_actual= float(input("Ingrese el año actual: "))
año_nacimiento= float(input("Ingrese su año de nacimiento: "))
#Procesos
edad= (año_actual - año_nacimiento)
#Salida
print("Su edad es:",edad)