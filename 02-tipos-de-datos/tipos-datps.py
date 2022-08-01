#NOTE Strings y numeros.

# palabra = 'Hola mundo' # string
# oracion = "Hola mundo comilla doble" #string

# entero = 20 # integer
# conDecimales = 20.2 # float
# complejo = 1j

# print(palabra, oracion, entero, conDecimales, complejo)


#NOTE Introduccion a listas.

# lista = [1, 2, 3]
# lista2 = lista.copy() # Crea una copia de una lista.
# lista.append(4) # Agrega un nuevo elemento a la lista.
# # lista.clear() # Borra la lista.
# print(lista, lista2)


#NOTE Contando elementos y calculando el largo de una lista.

# lista = [3, 2, 3]
# lista2 = lista.copy()
# lista.append(4)
# # print(lista, lista2.count(3)) 
# # print(len(lista), len(lista2))
# largoLista = len(lista)
# largoLista2 = len(lista2)

# print(largoLista, largoLista2)


#NOTE Accediendo a elementos de las listas.

# lista = ['Hola', 'Mundo', 'Chanchito feliz']
# lista2 = lista.copy()
# lista.append(4)

# print(lista[2])


#NOTE Eliminando elementos de una lista.

# lista = ['Hola', 'Mundo', 'Chanchito feliz']
# lista2 = lista.copy()
# lista.append(4)

# # lista.pop() #Elimina el ultimo elemento de la lista.
# lista.remove('Hola') #Elimina un elemento por su valor.
# print(lista)


#NOTE Reverse y sort

# lista = ['Hola', 'Mundo', 'Chanchito feliz']
# lista2 = lista.copy()
# lista.append('Chanchito triste')

# lista.reverse()
# lista.sort()
# print(lista)


#NOTE Tuplas

# lista = ['Hola', 'Mundo', 'Chanchito feliz']
# lista2 = lista.copy()
# lista.append('Chanchito triste')

# lista.reverse()
# lista.sort()
# tupla = ('hola', 'mundo', 'somos', 'tupla')
# listaDeTupla = list(tupla) # Transforma una tupla en una lista para poder modificarla.
# # # Metodos de tuplas.
# # print(tupla.count('hola'))
# # print(tupla.index('hola'))  #index('mundo') devuelve el indice de donde encontro mundo.
# listaDeTupla.append('chanchito')  
# print(listaDeTupla)


#NOTE Range

# lista = ['Hola', 'Mundo', 'Chanchito feliz']
# lista2 = lista.copy()
# lista.append('Chanchito triste')

# tupla = ('hola', 'mundo', 'somos', 'tupla')


# listaDeTupla = list(tupla)
# listaDeTupla.append('chanchito')  
# print(listaDeTupla)

# rango = range(6)
# print(rango)


# NOTE Introduccion a diccionarios

# lista = ['Hola', 'Mundo', 'Chanchito feliz']
# lista2 = lista.copy()
# lista.append('Chanchito triste')

# tupla = ('hola', 'mundo', 'somos', 'tupla')


# listaDeTupla = list(tupla)
# listaDeTupla.append('chanchito')  

# rango = range(6)

# diccionario = {
#     'nombre': 'Chanchito feliz',
#     'raza': 'Persa',
#     'edad': 5
# }

# # print(diccionario)
# # print(diccionario['nombre'])
# # print(diccionario['raza'])
# # print(diccionario.get('nombre'))
# diccionario['nombre'] = 'Floffy' #Para cambiar los valores de un diccionario.

# print(len(diccionario))


# NOTE Profundizando en diccionarios

# lista = ['Hola', 'Mundo', 'Chanchito feliz']
# lista2 = lista.copy()
# lista.append('Chanchito triste')

# tupla = ('hola', 'mundo', 'somos', 'tupla')


# listaDeTupla = list(tupla)
# listaDeTupla.append('chanchito')  

# rango = range(6)

# diccionario = {
#     'nombre': 'Chanchito feliz',
#     'raza': 'Persa',
#     'edad': 5
# }

# diccionario['nombre'] = 'Floffy' #Para cambiar los valores de un diccionario.

# print(len(diccionario))

# diccionario['ronronea'] = 'Si'
# print(diccionario)

# #REVIEW Formas de eliminar elementos de los diccionarios.
# # diccionario.pop('ronronea')
# # diccionario.popitem()
# # copiaGatito = diccionario.copy()  #Para copiar un diccionario.
# copiaGatito = dict(diccionario)
# # del diccionario['ronronea']
# diccionario.clear() #Para vaciar el diccionario.
# print(diccionario, copiaGatito)


#NOTE Diccionarios anidados y constructor dict.

fluffy = {
    "nombre": 'Fluffy',
    "edad": 4 
}

mamba =  {
    "nombre": 'Black Mamba',
    "edad": 12
}

gatitos = {
    "Fluffy": fluffy,
    "Mamba": mamba
}

print(gatitos)

perritos = dict(nombre="Chanchito Feliz", edad=6)
print(perritos)


verdadero = True
falso = False
print(verdadero, falso)