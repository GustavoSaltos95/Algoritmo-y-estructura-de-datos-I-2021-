
i = 1
try:
    palabra = input("Escriba una palabra: ")
    repeticiones = int(input("Escriba el numero de veces que se visualizara su palabra: "))

    while i<=repeticiones:
        print(f"-{i} {palabra}")
        i=i+1
except:
    print("error")            
        
