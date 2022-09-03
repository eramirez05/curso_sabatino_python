# Pedir la cantidad de grados y convertirlos a °C, °F y K.
#Entradas
from math import sqrt
entrada= float(input("Seleccione el número que corresponda al tipo de valor que desea convertir:\n 1:Celcius \n 2:Fahrenheit \n 3:Kelvin \n"))
conversion= float(input("Seleccione el número que corresponda al tipo de valor al que desea convertir:\n 1:Celcius \n 2:Fahrenheit \n 3:Kelvin \n"))
dato= float(input("Ingrese la cantidad a convertir: "))
salida= float
#Procesos
if entrada == 1:
    if conversion == 1:
        salida = dato
    else:
        if conversion==2:
            salida= ((dato* 9/5) + 32)
        else:
            if conversion==3:
                salida= (dato + 273.15)
            else:
                print("No ingresó valores correctos")
else:
    if entrada==2:
        if conversion==1:
            salida =((dato - 32) * 5/9 )
        else:
            if conversion==2:
                salida= dato
            else:
                if conversion==3:
                    salida= ((dato - 32) *5/9 + 273.15 )
                else:
                    print("No ingresó valores correctos")
    else:
        if entrada==3:
            if conversion==1:
                salida =(dato - 273.15)
            else:
                if conversion==2:
                    salida= ((dato -273.15) * 9/5 + 32 )
                else:
                    if conversion==3:
                        salida= dato 
                    else:
                        print("No ingresó valores correctos")
#Salidas
print("El resultado es: ", salida)
