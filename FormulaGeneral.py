#Obtener valores para: a, b y c. Calcular la fórmula general
#Entrada
from cmath import sqrt
import math


a= float(input("\nIngrese el valor de a:  \n"))
b= float(input("\nIngresa el valor de b:  \n"))
c= float(input("\nIngrese el valor de c:  \n"))
#Procesos

x1= ((- b - (pow ((b ** 2) - (4 * a * c), 1/2)))/ (2 * a))
x2= ((- b + (pow ((b ** 2) - (4 * a * c), 1/2)))/ (2 * a))

#Salida
print("Los valores que resuelven la ecuación son:")
print("X1 = ",x1)
print("X2 = ",x2)