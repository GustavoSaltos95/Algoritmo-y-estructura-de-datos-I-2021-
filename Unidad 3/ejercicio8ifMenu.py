"""
El programa debe:

Mostrar al usuario un menu
Permitir al usuario ingresar una opcion del menu
imprimir esa opcion
en caso de no escribir ninuna opcion del menu indicar ERROR
Condiciones:

imprimir (string)
1 (int)
2 (int)
salir (string)
Ayuda (como se comparan string y enteros cuidado con castear antes de verificar si el usuario ingreso str o int)
"""

try:
    opcion = input("""Ingrese una opcion
    -imprimir
    -1
    -2
    -salir
    """)
    if opcion.isalpha():#devuelve true si es alfabetico
        print(f"Opcion elegida : {opcion} ")

        if opcion == "imprimir":
           print("elegiste imprimir") 
        elif opcion == "salir":
            print("elejiste salir") 
        else:
            print("opcion alfabetica incorrecta.")  
    elif opcion.isdigit():# devuelve true si es numerico
        if int(opcion) == 1:
           print("elegiste la opcion 1.") 
        elif int(opcion) == 2:
            print("elejiste la opcion 2.") 
        else:
            print("opcion numerica incorrecta.")
    else:
        print("opcion ingresada incorrecta.")
 
except:
    print("error")        

