

# Ejercicio 1 ------------------------------------------------------------------------------------
# Cree un bucle 'for' de Python.

diccionario = {'Nombre': 'Inaki', 'Apellido': 'Mendigutxia', 'Edad': 39, 'Dirección': 'Plaza Basetxea 1 1º B', 'Municipio': 'Errenteria'}
n = 0
print('Datos del usuario\n')
for datos, valores in diccionario.items() :
    n += 1
    print(f'{n}. {datos}:  {valores}')

# Salida:

# Datos del usuario
# 1. Nombre:  Inaki
# 2. Apellido:  Mendigutxia
# 3. Edad:  39
# 4. Dirección:  Plaza Basetxea 1 1º B
# 5. Municipio:  Errenteria


# Ejercicio 2 ------------------------------------------------------------------------------------
# Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3

def suma(primero, segundo, tercero) :
    resultado = primero + segundo + tercero
    return resultado

print(suma(1, 2, 3))  # Salida: 6


# Ejercicio 3 ------------------------------------------------------------------------------------
# Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

suma = lambda primero, segundo, tercero : primero + segundo + tercero

print(suma(1, 2, 3))  # Salida: 6


# Ejercicio 4 ------------------------------------------------------------------------------------
# Utilizando la siguiente lista y variable, determine si el valor de la variable coincide
#  o no con un valor de la lista. Sugerencia, si es necesario, utilice un bucle for in
#  y el operador in.
#       nombre = 'Enrique'
#       lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

    # Opción 1: usando el método 'count()'

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']
num_apariciones = lista_nombre.count(nombre)
if num_apariciones > 0 :
    print(f"El nombre '{nombre}' está en la lista {num_apariciones} veces.")
else:
    print(f"El nombre '{nombre}' no está en la lista.")

# Salida: El nombre 'Enrique' no está en la lista.


    #Opción 2: usando el operador 'in'

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']
if nombre in lista_nombre :
    print(f"El nombre '{nombre}' está en la lista {num_apariciones} veces.")
else:
    print(f"El nombre '{nombre}' no está en la lista.")

# Salida: El nombre 'Enrique' no está en la lista.

    # Opción 3: usando un bucle 'for'

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']
num_apariciones = 0
for i in lista_nombre :
    if nombre == i:
        num_apariciones += 1
if num_apariciones > 0 :
    print(f"El nombre '{nombre}' está en la lista {num_apariciones} veces.")
else:
    print(f"El nombre '{nombre}' no está en la lista.")

# Salida: El nombre 'Enrique' no está en la lista.
