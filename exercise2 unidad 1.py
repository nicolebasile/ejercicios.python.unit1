"""Lógica Simple y Cortocircuito"""


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si al menos una de las variables es True.
"""

esta_lloviendo = True
riego_activado = True

piso_mojado = esta_lloviendo or riego_activado
print(piso_mojado)

assert piso_mojado


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el área es mayor a 5.
Restricción: Usar NOT.
"""

lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado, 2)

area_mayor_a_cinco = not (area_cuadrado <= 5)
print(area_mayor_a_cinco)

assert area_mayor_a_cinco


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el número 1 es divisible por 7 y al mismo tiempo el número 2 no lo es.
"""

numero_1 = 49
numero_2 = 50

es_divisible_1 = numero_1 % 7 == 0  # Verifica si el número_1 es divisible por 7
es_divisible_2 = numero_2 % 7 == 0  # Verifica si el número_2 es divisible por 7

resultado = es_divisible_1 and not es_divisible_2  # La expresión resultante
print(resultado)
assert resultado  # Asegura que la expresión sea True

"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
el mismo valor de la variable 3.
Restricción: sólo usar OR, NOT y el mecanismo de cortocircuito.
"""

variable_01 = False
variable_02 = True
variable_03 = 80
variable_04 = "90"
variable_05 = 100

resultado = (variable_01 or variable_02 or variable_03 or variable_04 or variable_05) or not (variable_01 and variable_02 and variable_03 and variable_04 and variable_05)
print(resultado)
