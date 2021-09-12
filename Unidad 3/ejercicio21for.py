"""El programa debe:
*     Preguntar al usuario una cantidad a invertir
*     Preguntar al usuario el interés anual y el número de años
*     Mostrar por pantalla el capital obtenido en la inversión cada año que dura la inversión"""

monto = float(input("Ingrese el monto a invertir: "))
años = int(input("Ingrese la cantidad de años a invertir: "))
interes = float(input("Ingrese la taza de interes para el plazo fijo: "))

for i in range(0,años):
    Ganancia = monto * interes /100
    monto = monto + Ganancia
    print(f"inversion obtenida en el año {i+1}: ${monto}")

