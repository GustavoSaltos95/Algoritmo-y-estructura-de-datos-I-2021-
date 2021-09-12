color1 = input("Ingrese el primer color primario: ").lower()
color2 = input("Ingrese el segundo color primario : ").lower()
try:
  
    if (color1 == "verde" and color2 == "rojo") or (color1 == "rojo" and color2 == "verde"):
        print(f"Los colores que ingresaste son: {color1} y {color2}\nLa combinacion de ambos colores resulta en Amarillo. ")
    elif (color1 == "azul" and color2 == "verde") or  (color1 == "verde" and color2 == "azul"):
        print(f"Los colores que ingresaste son: {color1} y {color2}\nLa combinacion de ambos colores es cian. ")
    elif (color1 == "rojo" and color2 == "azul") or (color1 == "azul" and color2 == "rojo"):
            print(f"Los colores que ingresaste son: {color1} y {color2}\nLa combinacion de ambos colores es magenta. ")
    else:
        print("Ingresaste un color invalido o repetiste el mismo color. ") 
except:
    print("ERROR")       
