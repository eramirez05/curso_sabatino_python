#Pedir el nivel del agua en metros de una cisterna
#Condiciones
#Si llega a mas de 6m-Desbordamiento de Agua
#Nivel 6m-Apagar bomba
#Entre 4 y 6-Desacelerar Bomba
#Entre 2 y 4- Bomba trabajando
#Entre o y 2-Acelerar bomba
#Nivel de 0- Encender Bomba
#Menor a 0- Fuga de Cisterna

#Entrada
nivel= float(input("Ingrese el nivel del agua en metros:  "))
#Procesos
if nivel>6:
    print("Apagar Bomba")
elif (nivel >= 4 and nivel <6):
    print("Desacelerar bomba")
elif (nivel>=2 and nivel <= 4):
    print("Bomba trabajando")
elif (nivel== 0):
    print ("Encender bomba")
elif nivel > 0:
    print("Fuga de Cisterna")
#Salidas