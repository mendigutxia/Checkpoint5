# Checkpoint nº 5: teoría


**1. ¿Qué es un condicional?**  
Un **condicional** en Python ( y en general, en cualquier lenguaje de programación, ya que es una estructura universal en todos ellos) es una expresión sintáctica que permite ejecutar porciones (bloques) de código de Python dependiendo del cumplimiento de una o varias **condiciones**.  Este tipo de estructuras es fundamental para el desarrollo de aplicaciones, ya que nos permiten controlar el flujo del programa: le damos 'inteligencia' a una aplicación, al hacer que tome diferentes caminos dependiendo de las condiciones. Esto hace que la aplicación que hayamos desarrollado se comporte diferente dependiendo de la entrada que le suministremos. Podemos decir que este tipo de estructuras son el primer paso de **inteligencia artificial** que se dió en programación.
La sintaxis de las estructuras condicionales existentes en Python son 3:

**Opción 1**  
```python
Sintaxis:

    if condición :  
        bloque a ejecutar si 'condición' es True


# Ejemplo

name = 'Jon'
if name ='Jon' :
    saludo = f'Hola, {name}, puedes acceder como Superusuario'
    print(saludo)

# Salida: Hola, Jon, puedes acceder como Superusuario'

```
**Opción 2**  
```python
Sintaxis:

    if condición :
        bloque a ejecutar si 'condición' es True
    else :
        bloque a ejecutar si 'condición' es False

# Ejemplo

autorizado = False
name = 'Jone'
if name == 'Jon' :
    autorizado = True
    saludo = f'Hola, {name}, puedes acceder como Superusuario'
    print(saludo)
else :
    print('Hola, no estás autorizado para acceder')

# Salida: Hola, no estás autorizado para acceder'

```
**Opción 3**  
```python
Sintaxis:

    if condición1 :
        bloque a ejecutar si 'condición1' es True
    elif condición2 :
        bloque a ejecutar si 'condición2'es True
    else :
        bloque a ejecutar si 'condición1' y 'condición2' son False

Para esta estructura, podemos usar tantos bloques elif como queramos, cada uno con su condición.

# Ejemplo

autorizado = False
name = 'Nerea'
if name == 'Jon' :
    autorizado = True
    saludo = f'Hola, {name}, puedes acceder como Superusuario'
    print(saludo)
elif name == 'Nerea' :
    autorizado = True
    saludo = f'Hola, {name}, puedes acceder como Superusuario'
    print(saludo)
else :
    print('Hola, no estás autorizado para acceder')

# Salida: Hola, Nerea, puedes acceder como Superusuario

```

En los 3 casos, si alguna de las condiciones es True, no se evalúan el resto de las condiciones posteriores que pueda haber, saltando el flujo del programa a la primera línea después del bloque condicional.

**2. ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?**  
Los bucles son estructuras de control fundamentales en programación, ya que nos permiten controlar el flujo de una aplicación, repitiendo la ejecución de un bloque de código en diferentes situaciones (iteración).  
Son muy útiles porque nos puede permitir procesar gran cantidad de datos, realizando complejas operaciones con pocas líneas de código.  
 Existen 2 tipos de bucles en Python
 1. **Bucle 'for'**  
 El bucle 'for' se usa para recorrer iterables (tipos de python compuestos de varios elementos) y ejecutar un bloque de código; iterables son los strings, las listas, las tuplas, los diccionarios, los rangos y los sets. El bucle 'for' nos permite coger todos y cada uno de los elementos del iterable y ejecutar un mismo bloque de código a cada uno de ellos.

 ```python
 Sintaxis:

for variable in iterable :
    bloque de código a ejecutar  

# Ejemplo:

diccionario = {'Nombre': 'Inaki', 'Apellido': 'Mendigutxia', 'Edad': 39, 'Dirección': 'Plaza Basetxea 1 1º B', 'Municipio': 'Errenteria'}
n = 0
print('Datos del usuario\n')
for datos, valores in diccionario.items() :
    n *= 1
    print(f'{n}. {datos}:  {valores}')
    

# Salida:

# Datos del usuario
# 1. Nombre:  Inaki
# 2. Apellido:  Mendigutxia
# 3. Edad:  39
# 4. Dirección:  Plaza Basetxea 1 1º B
# 5. Municipio:  Errenteria
```



 2. **Bucle 'while'**  
 El bucle while nos permite ejecutar un bloque de código repetidamente mientras sea **verdadera** una cierta condición.
 ```python
 Sintaxis  
 while condición :
    bloque de código a ejecutar  

# Ejemplo: muestra en pantalla los 5 primeros elementos de una lista

n = 0
lista = ['naranja', 'pera',' manzana', 'mandarina', 'melocotón', 'aguacate'] 
while n < 5 :
    print(lista[n])
    n += 1


# Salida:

# naranja
# pera
# manzana
# mandarina
# melocotón
```

**3. ¿Qué es una lista por comprensión en Python?**  
Una lista por comprensión en Python es una manera compacta de crear nuevas listas a partir de iterables. Proporciona una sintaxis más compacta y legible que los bucles 'for' tradicionales para crear listas basadas en transformaciones o filtros aplicados a los elementos de un iterable. Se usan cuando la trasformación o el filtro a aplicar se pueden expresar en una línea, es decir, no son complejos.
```python
Sintaxis

[expresión for elemento in iterable if condición]

# Ejemplo 1: creamos una una nueva lista que suma 5 a cada elemento de la original

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nueva_lista = [elemento + 5 for elemento in lista]
print(cuadrados)   # Salida: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Ejemplo 2: creamos una una nueva lista con los elementos de la original en mayúsculas,
# si el elemento tiene más de 7 caracteres

lista = ['naranja', 'pera',' manzana', 'mandarina', 'melocotón', 'aguacate']
nueva_lista = [elemento.upper() for elemento in lista if len(elemento) > 7]
print(nueva_lista)   # Salida: [' MANZANA', 'MANDARINA', 'MELOCOTÓN', 'AGUACATE']

```

**4. ¿Qué es un argumento en Python?**  
Un argumento en Python es un concepto que se usa relacionado con los métodos y las funciones. *Funciones* son bloques de código que encapsulamos y a las que les damos un nombre. De esta manera, podemos llamar a estos bloques para ejecutarlos en diferentes puntos de nuestra aplicación, sin tener que repetir ese código: a eso se le llama reutilización del código y nos permite construir aplicaciones más compactas y más fáciles de entender. Estas funciones pueden tener (de hecho, la mayor parte de las veces los tienen) **argumentos**, que nos permiten pasar a estos bloques encapsulados variables para que el bloque de código que contienen sea ejecutado con esos valores. Veámoslo con un ejemplo: vamos a definir una función sencilla que sume dos valores. 
```python
def funcion_suma(primer_sumando, segundo_sumando) :
    suma = primer_sumando + segundo_sumando
    return suma

print(funcion_suma(45, 15))   # Salida: 60
```
En este caso, los **argumentos** de 'funcion_suma' son **primer_sumando** y **segundo_sumando** y se encierran entre paréntesis. Estos argumentos nos permiten pasar a la función cualquier valor que deseemos. De esta manera, podemos usar esta función en cualquier parte de nuestra aplicación y con cualquier par de valores. Esto nos da una enorme flexibilidad.

**5. ¿Qué es una función Lambda en Python?**  
Una función lambda es una función especial que se define de forma sencilla en una sola línea y es anónima, aunque pueda ser asignada a una variable. Nos permite definir funciones sencillas y muy compactas. Veamos un ejemplo con el caso anterior de suma de 2 valores.
```python
Sintaxis

lambda argumentos : expresión

# Ejemplo
suma = lambda sumando1, sumando2 : sumando1 + sumando2
print(suma(45, 15))   # Salida: 60
```
Como vemos, es la misma función que en el punto anterior, pero definida con un formato en una sola línea, mucho más compacto. Se recomiendan cuando la expresión es una operación sencilla que se puede expresar en una sola línea y al ser anónima no necesite usarse en otras partes de la aplición. En nuestro ejemplo la hemos asignado a una variable y podríamos usarla en otra parte, pero no tiene por qué ser así.  
Si el bloque de código de la función consta de varias líneas, o lo vamos a usar en otras partes del código, es mejor usar una función regular, del tipo explicado en el punto anterior.


**6. ¿Qué es un paquete pip?**

Los paquetes pip son librerias desarrolladas por programadores que añaden funcionalidades a la base de Python. Cuando instalamos Python en una máquina viene con un conjunto básico de componentes (tipos de objetos, funciones, operadores, métodos, clases,...) que son los llamados objetos built-in. Pero con el tiempo, los desarrolladores de Python han ido desarrollando bibliotecas que aumentan enormemente las funcionalidades de Python. **PIP** es una aplicación de consola que nos permite gestionar los paquetes que necesitemos instalar en nuestra máquina para su uso. De esta manera, con el comando **pip** podemos instalar en nuestra máquina el paquete que necesitemos y así podemos usar sus funciones, métodos y clases sin tener que crearlos desde cero. Existen infinitos paquetes desarrollados por la comunidad Python para múltiples áreas: machine learning, ciencia de datos, representaciones gráficas, deep learning, tratamieto de textos, reconocimieto de caracteres,... Esta enorme aportación de la comunidad Python hace que este lenguaje sea uno de los más potentes y desarrollados.

Sería una locura instalar todos los disponibles al existir cientos (si no miles de ellos) que ocuparían todo el disco duro de nuestro ordenador. El repositorio centralizado de paquetes Python se encuentra en la URL https://pypi.org/, donde podemos buscar el que se ajuste a nuestras necesidades. Por ese motivo cada programador instala y activa los que necesita para su trabajo, usando el comando **pip**.  

Para instalar un paquete, éste se instalaría localmente en nuestra máquina así:
```
pip install nombre_del _paquete
```


Por ejemplo, para instalar SQLAlchemy, que es un paquete para gestionar bases de datos SQL, usaríamos el siguiente comando en la consola de Windows:  
```
pip install sqlalchemy
```


