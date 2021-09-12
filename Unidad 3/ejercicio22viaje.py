"""El programa debe:
*    Pedir al usuario una cantidad de tramos de un viaje
*    Pedir al usuario la duración en minutos de cada tramo
*    Calcular el tiempo total de viaje
*    No deben generar errores"""


acumulador = 0
try:
    tramos = int(input("Ingrese la cantidad de tramos: "))    
    for i in range(0,tramos):
        tiempo = int(input(f"Ingrese el tiempo en minutos del tramo: {i+1}\n "))
        acumulador = acumulador + tiempo
    print(f"Recorrio {tramos} tramos en un tiempo total de {acumulador} minutos. ")  
except:
    print("Porfavor ingrese numeros enteros.")      

