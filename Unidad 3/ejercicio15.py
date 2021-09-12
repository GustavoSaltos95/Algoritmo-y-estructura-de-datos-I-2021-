###**Ejercicio (Ahora con flag)**
'''El programa debe:
*  pedir un dato al usuario
*  solo en caso que este escriba la palabra clave "python" imprimir por pantalla "Correcto", en caso contrario debe seguir pidiendo el dato
*  no deben aparecer errores.
'''
flag = True
while flag:
    var1 = input("Ingrese un dato. ")
    if var1 == "python":
        print("Correcto.")
        flag = False
