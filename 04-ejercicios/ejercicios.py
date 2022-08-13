# dato = input('Ingrese dato: ')

# # print(dato)
# lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

# # Si es que nuestra lista contiene uno de estos elementos, contamos el dato que ingresamos.
# if lista.count(dato) > 0:  # si nuestra lista contiene mas de un solo elemento interpretamos que el dato existe.
#     print('El dato existe:', dato)
# else:
#     print('El dato no existe:(', dato)


dato = input('Ingrese un dato: ')

lista = ['hola', 'chanchito', 'feliz', 'dragones']

if lista.count(dato) > 0:
    print('El dato existe: ',dato)
else:
    print('El dato no existe!')