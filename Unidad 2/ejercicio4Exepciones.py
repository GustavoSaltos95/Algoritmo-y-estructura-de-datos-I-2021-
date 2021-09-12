"""
El programa debe :
0pedir por teclado el dinero actual de una persona
pedir por teclado el precio del insumo que quiere comprar en USD
convertir ese dinero a dolares( 1USD -> 170$)
devoler por pantalla True en caso que pueda comprar, False en caso que no
No deben aparecer errores
"""
try:
    DineroCliente = float(input('ingrese la suma de dinero que tiene en pesos. '))
    PrecioInsumo = float(input('ingrese el precio del insumo en dolares. '))
    DineroClienteUsd = DineroCliente / 170
    print(DineroClienteUsd >= PrecioInsumo) #esta operacion devuelve True o False
except:
    print('Dato ingresado no valido. ')    #manejo de errores intrenta todas las acciones del try, si hay datos no validos o operaciones imposibles entra por except




