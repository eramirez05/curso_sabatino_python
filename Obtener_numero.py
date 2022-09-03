#Obtener un número y determinar lo siguiente:
#a) si es negativo y mayor a -100 imprimir los números impares de forma DESCENDENTE
#b) si es positivo y menor a 100 mostrar los números pares de forma ASCENDENTE
#c) en otro caso imprimir No Válido
#ENTRADA


numero= float(input("Ingrese un número: "))

#PROCESO Y SALIDAS
while(numero <0 and numero > -100):
    numero +=1 
    if numero %2 ==1:
         print("Los numero impares son: ",numero)
    numero +=1 
while (numero>0 and numero < 100):
    if numero %2 ==0:
        print("Los numeros pares son: ",numero)
    numero -=1
if(numero <-100 and numero> 100):
    print("No valido")

