"""Listas"""

"""
Inicializar una lista vacía y luego agregarle 4 elementos cualquiera
Restricción: Utilizar el método append
"""
lista_01 = []

lista_01.append('camilla', )
lista_01.append('doctor', )
lista_01.append('enfermera', )
lista_01.append('pastillas')

assert len(lista_01) == 4


"""
Extraer el cuarto elemento de la lista
Restricción: Utilizar el método pop
"""

lista = ["ho", "la", 81, 6, 42, "como", "estas?"]
lista = lista.pop ()
elemento_extraido = 6

assert elemento_extraido == 6


"""
Concatenar las siguientes listas
Restricción: Utilizar el método extend
"""

lista_a = [1, 2, 3]
lista_b = ["4", "5", "6"]
lista_c = ["siete", "ocho", "nueve"]

lista_a.extend(lista_b) #no retorna una nueva lista con los cambios, modifica la existente
lista_a.extend(lista_c)

assert lista_a == [1, 2, 3, "4", "5", "6", "siete", "ocho", "nueve"]


"""
Agregar la variable variable_01 en la segunda posición de la lista lista_nueva
Restricción: Utilizar el método insert
"""

variable_01 = 2
lista_nueva = [0, 1, 3, 4]

lista_nueva.insert(2, variable_01)

assert lista_nueva == [0, 1, 2, 3, 4]


"""
Armar una lista que contenga el primer y el último elemento de la siguiente lista
Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, 42, 81, 6, "la"]

lista_primero_y_ultimo = [] #creamos una vatiable sin definir los elementos de la lista
lista_primero_y_ultimo.append(lista[0])  # agregamos a la nueva variable los elementos que querramos de 'lista', indicando la posición
lista_primero_y_ultimo.append(lista[5])

assert lista_primero_y_ultimo == ["ho", "la"]


"""
Armar una lista que contenga los primeros 3 elementos de la siguiente lista
Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, "la", 81, 6, 42]

lista_primeros = []
lista_primeros.append(lista[0])
lista_primeros.append(lista[1])
lista_primeros.append(lista[2])

assert lista_primeros == ["ho", 3.1416, "la"]


"""
Armar una lista que contenga los primeros 3 elementos de la siguiente lista
Restricción: Utilizar indexado múltiple
"""

lista = ["ho", 3.1416, "la", 81, 6, 42]
del lista[3]
del lista[4]
del lista[-1]

lista_primeros = lista
assert lista_primeros == ["ho", 3.1416, "la"]

"""
Armar una lista que contenga los primeros 2 y los últimos 2 elementos de la
siguiente lista
Restricción: Utilizar el método extend junto al indexado múltiple
"""

lista = ["ho", "la", 81, 6, 42, "como", "estas?"]
lista_primeros_y_ultimos = []
lista_primeros_y_ultimos.extend(lista[:2])
lista_primeros_y_ultimos.extend(lista[-2:])

assert lista_primeros_y_ultimos == ["ho", "la", "como", "estas?"]


"""
Concatenar las siguientes 2 listas
Restricción: Utiliar el operador +
"""

lista_01 = [0, 1, 2, 3]
lista_02 = [5, 6]

lista_concatenada = lista_01 + lista_02

assert lista_concatenada == [0, 1, 2, 3, 5, 6]

"""
Concatenar 3 veces la siguiente lisa consigo misma
Restricción: Utiliar el operador *
"""

lista_01 = [0, 1, 0, 1, 0, 1]

lista_duplicada = lista_01 * 3

assert lista_duplicada == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]


"""
Verificar si el siguiente elemento pertenece a la lista
Restricción: Utiliar el operador in
"""

elemento = 1.0
lista = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1.0, 1, 0, 1, 0, 1]

variable_booleana = elemento in lista

assert variable_booleana


"""
Verificar si las siguientes listas son iguales
Restricción: Utilizar el operador ==
"""

lista_01 = [1, 2, 3, 4.5, 6, 7]
lista_02 = [1, 3, 2, 4, 5, 6, 7]

son_iguales = lista_01 == lista_02

assert not son_iguales


"""
Se cuenta con una lista de elementos booleanos que corresponden a las notas de los exámenes
cuatrimestrales de un alumno (True si está aprobado y False en caso contrario)
Determinar si el alumno no tiene examenes aprobados.
Restricción: Utilizar el método any
"""

notas = [False, False, False, False, False, False, False, False, False]

no_tiene_examenes_aprobados = True

if True in notas:
    print("Tiene un examen aprobado")
else:
    no_tiene_examenes_aprobados is True
    print(no_tiene_examenes_aprobados)
    
assert no_tiene_examenes_aprobados


"""
Se cuenta con una lista de elementos booleanos que corresponden a las notas de los exámenes
cuatrimestrales de un alumno (True si está aprobado y False en caso contrario)
Determinar si el alumno ha aprobado todos sus exámenes.
Restricción: Utilizar el método all
"""

notas = [True, True, False, True, True, True, True, True, True, True, True, True]

tiene_todo_aprobado = notas

if notas != False:
    print(False)
else:
    notas == True
    print(True)
assert not tiene_todo_aprobado #arreglar