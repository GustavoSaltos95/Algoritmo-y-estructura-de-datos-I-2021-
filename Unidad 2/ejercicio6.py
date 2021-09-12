""""
El programa debe:
- pedir en orden el Nombre, apellido, edad y numero de calzado
- verificar que cada uno sea el tipo de variable correcto (IMPORTANTE)
- en caso verdadero imprimir de la siguiente manera el resultado:

ejemplo

Nombre: Lionel

Apellido: Messi

Edad: 34

Numero de Calzado: 42.5

- en caso contrario imprimir error"""


try:
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    talle = float(input("Ingrese su talle de calzado: "))
    
    print(f"Nombre: {nombre}\nApellido:{apellido}\nEdad:{edad}\nTalle de calzado:{talle}" )

except: 
    print("Uno de los datos ingresados no es valido. ")   
