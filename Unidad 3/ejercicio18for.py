frase = input("Escriba una frase: ")
letra = input("Escriba una letra para contar en su frase: ")
contador = 0
for i in frase:
    if i == letra:
        contador = contador+1
print(f"La letra {letra} aparece {contador} veces en su frase. ")        