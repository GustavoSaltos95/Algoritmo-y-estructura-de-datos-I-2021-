'''
El programa debe :
*   Almacenar una variable `contraseña` con una contraseña
*   Preguntar al usuario por la contraseña e imprimir por pantalla si la contraseña introducida por el usuario coincide o no con la variable
 **IMPORTANTE**: sin tener en cuenta mayúsculas y minúsculas.(metodos string)
*   no debe generar errores
'''
contrasenia = "AutitoVerde"
try:
    login = input("Ingrese su contraseña:  ")
    if contrasenia.upper() == login.upper(): #este metodo convierte toda la cadena a mayusculas
        print("Contraseña correcta.")
    else:
        print("Contrasea incorrecta.")
except:
    print("dato no valido")            