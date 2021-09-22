"""##**Ejercicio 5.7 (Estadisiticas)**
El programa debe:
*   Simular un programa que calcule estadisticas
*   Pedir al usuario una serie de numeros enteros el 1 al 10 (verificar) y guardarlos en una lista, hasta que el usuario ingrese "fin"
*   Luego mostrar un menu con 4 opciones
  1.  Calcular promedio
  2.  Verificar cuantos numeros son menores que el numero indicado por el usuario
  3.  Verificar cuantos numeros son mayores o igual que el numero indicado por el usuario
  4.  Verificar si un numero que desee el usuario esta en la lista
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio"""
def pedirnumero():
    listanumeros = []
    contador = 1
    while True:    
        datoIngresado = input(f"ingrese el numero {contador} entre (1-10) o escriba fin para terminar. ")
        if datoIngresado == "fin":
            break
        else:
            try:
                if int(datoIngresado) > 0 and int(datoIngresado) <= 10:
                    listanumeros.append(int(datoIngresado))
                    contador = contador + 1
                else:
                    print('Dato erroneo. ')       
            except:
                print('Dato erroneo. ')  
    return listanumeros

def promedios(listaPrincipal):
    sumatotal = sum(listaPrincipal)
    numerototal = len(listaPrincipal)
    return round(sumatotal/numerototal,2)

def numerosmenores(listaPrincipal):
    while True:
        try:
            comparador = int(input('escriba el numero para comprar'))
            break
        except:
            print('Escriba un numero. ')
    contador = 0
    for i in listaPrincipal:
        if i < comparador:
            contador = contador + 1
    return contador

def numero_en_lista(listaPrincipal):
    while True:
        try:
            numero_comparar = int(input("Indique el numero a buscar: "))
            break
        except:
            print("Dato Incorrecto!")
    if numero_comparar in listaPrincipal:
        contador=True
    else:
        contador=False
    return contador    




listaPrincipal = pedirnumero()
print(listaPrincipal)
print(f'el promedio de la lista es: {promedios(listaPrincipal)}')
