"""
Agencia de autos:

El programa cuenta con tres marcas de autos y su precio.

El programa debe:

pedir al usuario que ingrese la cant de dinero que dispone.
verificar que la cantidad ingresada sea un numero y sino mostrar error
verificar la cantidad de ingresada e indicar que auto o autos puede comprar
Ford = 10000
Renault = 11000
Chevrolet = 15000
"""
Ford = 10000
Renault = 11000
Chevrolet = 15000


try:
    DineroCliente = float(input("Ingrese el dinero que usted tiene disponible."))
    if DineroCliente >= Chevrolet:
        print("Usted puede puede elegir cualquiera de los 3 vehiculos.")
    elif DineroCliente >= Renault:
        print("Usted puede optar por Renaul o Ford.")    
    elif DineroCliente >= Ford:
        print("Solo podes comprar Ford.")
    else:
        print("Usted no puede comprar ningun vehiculo.")  
except:
    print("Debe ingresar un numero.")    