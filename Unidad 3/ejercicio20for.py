"""El programa debe:
*    Pedir al usuario un número entero positivo y mostrar por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

Ej: num = 8.

8,7,6,5,4,3,2,1
"""
num1 = int(input("Ingrese un numero entero positivo: "))
for i in range(num1,-1,-1):
    print(i,end=",")