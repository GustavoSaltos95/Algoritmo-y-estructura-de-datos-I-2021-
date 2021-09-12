try:
    color1 = input("ingrese el primer color primario: ")

    if color1 == "rojo":
        color2 = input("ingrese el segundo color primario: ")
        if color2 == "azul":
            print(f"Los colores que eligio son : {color1} y {color2}\nLa mezcla de ambos resulta en magenta.")
        else:
            print(f"Los colores que eligio son : {color1} y {color2}\nLa mezcla de ambos resulta en amarillo.")    
    else:
        color2 = input("ingrese el segundo color primario: ")   
        if color2 == "verde":
            print(f"Los colores que eligio son : {color1} y {color2}\nLa mezcla de ambos resulta en cyan.") 
        else:
            print(f"Los colores que eligio son : {color1} y {color2}\nLa mezcla de ambos resulta en magenta.")
except:
    print("ERROR")