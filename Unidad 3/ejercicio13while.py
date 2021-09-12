'''
El programa debe:
*  pedir al usuario 5 datos numericos
*  verificar que sean enteros y sino pedir nuevamente los 5
*  cuando se tenga los 5 datos el programa debe devolver el promedio
*  no deben aparecer errores.
'''
i = 1
total = 0
while i<=5:
    try:
        num=float(input(f"Ingrese el numero {i} : "))
        i=i+1
        total= total+num
    except:
        print("error")
print(f"El promedio final es : {total/5}")                
