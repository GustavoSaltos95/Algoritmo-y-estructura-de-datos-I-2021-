'''##**Ejercicio 5.3**
Crear una funcion que debe:

*    Pedir al usuario 5 materias (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
*    Verficiar que sea un nombre correcto
*    Almacenar los nombres en una lista
*    Mostrar las materias en orden alfabetico
*    No deben aparecer y se deben tener en cuenta todos los posibles errores'''
def ordenadorDePalabras():
    listaMaterias = []
    for i in range(5):
        while True:
            materia = input(f'Ingrese el nombre de la materia {i+1} ')
            if materia.isalpha():
                listaMaterias.append(materia)
                break
            else:
                print('Solo se admiten nombres de materias. ')
    listaMaterias.sort()
    print(listaMaterias)
ordenadorDePalabras()