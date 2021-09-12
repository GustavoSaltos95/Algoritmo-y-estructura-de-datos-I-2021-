'''##**Ejercicio 5.1**
Crear una funcion que debe: (usar listas)

*    Pedir al usuario cantidad de personas
*    Pedir al usuario una a una la edad de las personas
*    Finalizado la carga de las edades debe imprimir por pantalla la edad mayor
*    No deben aparecer y se deben tener en cuenta todos los posibles errores'''
try:
    personas = int(input('Ingrese la cantidad de personas: '))
    
    edades = []
    for i in range(0,personas):
        while True:
            try:
                edadesingresadas = int(input(f'Ingrese la edad de la persona #{i+1}: '))
                edades.append(edadesingresadas)
            except:
                print('debe ingresar un numero')    
    edades.sort()
    print(f'La edad mayor ingresada es {edades[-1]}\nLa lista completa es: {edades}') 
except:
    print('Tenes que escribir un numero.')       
