'''Crear una funcion que debe:
Tener almacenado el abcedario en una lista
Pedir al usuario un numero (2 o 3) - VERIFICAR que el num ingresado sea 2 o 3
Elimina de la lista las letras que ocupen posiciones múltiplos de ese numero
Mostrar por pantalla la lista resultante.
No deben aparecer y se deben tener en cuenta todos los posibles errores'''
def abcmultiplos():
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    try:
        numeroingresado = int(input('Ingrese 2 o 3 '))
        if numeroingresado == 2 or numeroingresado == 3:
            for i in range(numeroingresado,len(abc),numeroingresado):
                print(abc[i-1])
        else:
            print('solo puede ingresar 2 o 3')
    except:
        print('debe ingresar un numero') 
abcmultiplos()               