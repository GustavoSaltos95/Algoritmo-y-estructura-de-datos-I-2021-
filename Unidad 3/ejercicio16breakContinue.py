#sentencia BREAK permite finalizar un bucle al igual que un flag
#sentencia CONTINUE nos permite saltar a la siguiente iteracion sin romper el bucle
"""El programa debe:
*   mostrar el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
*  si el usuario escribe "hola" o "chau" que no se haga el eco"""

while True:
    var1 = input("Escriba lo que guste o escriba salir para finalizar: ").lower()
    if var1 == "salir":
        break #si se cumple la condicion del if se ejecuta el break y esto fuerza el fin del bucle
    elif var1 == "hola" or var1 == "chau":
        continue #si se cumple esta condicion el bucle sigue ejecutandose 
    else:
        print(f"{var1}")