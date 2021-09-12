temperatura = float(input("Ingrese su temperatura  "))
print(f"tu temperatura: {temperatura}")

if temperatura >= 37.5:
    print("Tenes fiebre.")
elif temperatura <= 30:
    print("tenes hipotermia.")
else:
    print("esta todo ok.")    
