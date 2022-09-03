#Programa que calcula el promedio de 3 calificaciones y dice si es reprobado o aprobado
#Entrada
from math import sqrt

calificacion_1= float(input("Escriba la primer calificación: "))
Calificacion_2= float(input("Escriba la segunda calificación: "))
calificacion_3= float(input("Escriba la tercer calificación: "))
#Declarar constante
divisor = 3
#Procesos
suma= calificacion_1 + Calificacion_2 + calificacion_3
promedio= suma/divisor
if promedio>5:
    print("Usted se encuentra APROBADO")
else :
    print("Usted se encuentra REPROBADO")
#Salida
print("El promedio obtenido es: ",promedio)

