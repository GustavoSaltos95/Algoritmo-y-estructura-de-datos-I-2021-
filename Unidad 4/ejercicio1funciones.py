"""###**Ejercicio 4.1 (Calculadora)**
El programa debe:
*   Contar con 4 funciones (suma, resta, división y multiplicación)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los dos numero para operar y devolver el resultado al usuario
*   Gestionar posibles errores"""
def sumador(a,b): #definimos la funcion a y b son los parametros
    suma = float(a)+float(b)
    return  suma #return es lo que nos devolvera esta funcion cuando la llamemos

def restador(a,b):
    resta = float(a)-float(b)
    return  resta

def divisor(a,b):
    if b != 0:
        division = float(a)/float(b)
        return  division
    else:
        return  "No podes dividir por 0"   
    

def multiplicador(a,b):
    multiplicacion = float(a)*float(b)
    return  multiplicacion

def pedirNumero():
    while True:
        try:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            break
        except:
            print("ERROR")    
    return num1,num2

while True:
    condicion=input("Por favor ingrese una opcion:\n1-suma\n2-resta\n3-multiplicacion\n4-divicion\n5-salir: ")
    if condicion == "1":
        a,b = pedirNumero() #guardamos en a y b los valore que pedimos en la funcion anterior
        print (f"La suma de {a} + {b} = {sumador(a,b)}")
    elif condicion == "2":
        a,b = pedirNumero()
        print (f"La resta de {a} - {b} = {restador(a,b)}")
    elif condicion == "3":
        a,b = pedirNumero()
        print(f"La multiplicacion entre {a} y {b} = {multiplicador(a,b)}") 
    elif condicion == "4":
        a,b = pedirNumero()
        print(f"La divicion entre {a} y {b} = {divisor(a,b)}")
    elif condicion == "5":
        break

    else:  
        print("Opcion incorrecta.")                    
    