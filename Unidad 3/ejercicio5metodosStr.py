'''
El programa debe :
*    Pedir al usuario un string
*    Determinar si una cadena esta en minusculas o mayusculas
'''
try:
    texto = str(input("Escriba un texto en mayuscula o minuscula."))
    if texto.isupper(): #este metodo determina si todos los caracteres son mayusculas.
        print("Todos los caracteres son mayusculas")
    elif texto.islower():
        print("Todos los caracteres son minusculas")
    else:
        print("Hay mayusculas y minusculas mezclados.")

except:
    print("Debe ingresar un texto.")