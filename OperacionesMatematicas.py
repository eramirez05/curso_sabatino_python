# EJEMPLO 2. OPERACIONES MATEMÁTICAS
# IMPORTAR BIBLIOTECAS QUE CONTIENEN FUNCIONES MATEMÁTICAS
import math

#ENTRADAS DE DATOS
#Declarar o declarar las variables
from math import sqrt


numero1 = float(input("Escribe el 1er número: "))
numero2 = float(input("Escribe el 2do numero: ") ) 

#Declara una Constante
PI = 3.1416
#PROCESOS (Calculos u operaciones Matematicas y/o lógicas)
suma = numero1 + numero2
resta = numero1 - numero2 
multiplicación = numero1*numero2
division = numero1/numero2
potencia1 =numero1 ** numero2
potencia2= pow(numero1, numero2)
cuadrado = numero1 **2
cubo = pow(numero2,3)
raiz_cuadrada = math.sqrt(9)
raiz_cuadrada2 = pow (9,1/2)
raiz_cubica = pow (27,1/4)
modulo_residuo = numero1 % numero2

#SALIDA DE DATOS
print("La suma es igual=", round(suma,2))
print("La suma es =" + str (suma)) #CONCATENACIÓN ()
print(f"La suma es = {suma}") #f (formatear el texto )
print("La resta es igual =",resta)
print("La division es igual =", division)
print("La multiplicacion es igual = ", multiplicación)
print("La potencia 1 es igual=",potencia1)
print("La potencia 2 es igual= ",potencia2)
print("El cuadrado es igual=",cuadrado)
print("El cubo es igual=",cubo)
print("La raiz cuadrada es igual=",raiz_cuadrada)
print("La raiz cuadrada 2 es igual= ",raiz_cuadrada2)
print("La raiz cubica es igual =",raiz_cubica)
print("EL residuo es igual =",modulo_residuo)