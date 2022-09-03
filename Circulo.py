#Programa que calcula el perimetro y area de un circulo 
#Entradas
radio= float(input("Intruzcas el radio del circulo:"))
pi=3.1416 #constante

#Procesos
area= pi*(radio**2)
perimetro= pi*(2*radio)
#Salidas
print("El área del ciruclo es = ",area)
print("El diametro del circulo es igual=",perimetro)