"""**Ejercicio**
El programa debe:
*   Pedir al usuario una palabra
*   Verificar que sea una palabra y no un numero
*   Mostrar por pantalla las letras una a una
*   No producir errores"""
while True:
    try:
        palabra = (input("Ingrese una palabra: "))
        if palabra.isnumeric(): 
            print("te pedi una palabra ")
        else:
            for i in palabra:
                print(i)
            break    
    except:
        print("ERROR")                  