
acumulador = 0
duracionTramos = []
try:
    tramos = int(input("Ingrese la cantidad de tramos: "))    
    for i in range(0,tramos):
        duracionTramos.append(int(input(f"Ingrese el tiempo en minutos del tramo: {i+1}\n ")))
        acumulador = acumulador + duracionTramos[i]
    print(f"Recorrio {tramos} tramos en un tiempo total de {acumulador} minutos o {acumulador/60}. ")  
except:
    print("Porfavor ingrese numeros enteros.")