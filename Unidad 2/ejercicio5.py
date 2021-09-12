""""
El programa debe:
- pedir dos datos por consola
- verificar que los dos datos sean numeros enteros
- en caso verdadero imprimir la suma de ambos
- en caso contrario imprimir error
"""
try:
    num1 = int(input("ingrese un numero entero : "))
    num2 = int(input("ingrese otro numero entero : "))
    print(num1 + num2)
except:
    print("dato ingresado no valido. ")    

