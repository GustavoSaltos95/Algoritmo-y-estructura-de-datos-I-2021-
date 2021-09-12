try:
    nota1 = float(input("Ingrese la primera nota."))
    nota2 = float(input("Ingrese la segunda nota."))
    nota3 = float(input("Ingrese la tercera nota."))
    print(f"El promedio final es : {round((nota1 + nota2 + nota3) / 3,2)} ") #la funcion round es para redondear un valor. el ,2 del final indica la cantidad de decimales que tendra el redondeo

except:
    print("alguna nota ingresada es incorrecta")