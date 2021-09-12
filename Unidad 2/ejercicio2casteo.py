a = "2"
b = "3"

c = int(a)+int(b) #int(a) transforma mi variable string (a) a una variable entera

print(f"la suma de {a} y {b} es {c}")

num1 = int(float(input("ingrese num 1 "))) #doble casteo, convertimos string en float y luego ese float a entero
num2 = int(float(input("ingrese  num 2 ")))
print(num1 + num2)