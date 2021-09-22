'''##**Ejercicio 5.2**
Crear una funcion que debe:

*    Pedir al usuario una palabra o una frase
*    Indicar si esta se trata de un palindromo (reconocer, neuquen, amor a roma)
*    No deben aparecer y se deben tener en cuenta todos los posibles errores'''


datostr = input('ingrese una plabra o frase: ')
lista = list(datostr) 
if not datostr.isalpha():
    print("palabra incorrecta ")
else:  
    pass