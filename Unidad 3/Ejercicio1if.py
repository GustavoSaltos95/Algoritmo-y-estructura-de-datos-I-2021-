"""
El programa debe:

- pedir el ingreso de un número positivos al usuario y almacenar la respuesta en la variable numero.
- Verificar que se trate de un numero entero y sino mostrar un error
- Comprobar si el número es negativo. Si lo es, el programa debe avisa que no era eso lo que se había pedido. (si no hay error)
- Finalmente imprimir siempre el valor introducido por el usuario.(si no hay error)
"""
try:
    num1 = int(input("Ingrese un numero entero y positivo: "))
    if num1 < 0: #verifica si el numero es negativo, esta linea siempre termina en ":" y si solo se ingresa un valor sin ningun operador este lo toma como verdadero
        print("Tenes que ingresar un numero positivo!")
        #se puede usar "pass" esto sirve para que simplemente no haga nada
    else:
        print("El numero ingresado es positivo") 
    print(f"El numero ingresado es {num1}")

except:
    print("El numero ingresado no es entero")    
