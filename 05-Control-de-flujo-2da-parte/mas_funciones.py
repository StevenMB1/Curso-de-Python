def miFuncion2(argumento = 'chanchito'):
    print(argumento)
    
# miFuncion2('Batman')
# miFuncion2()

def miFuncionLista(lista):
    for el in lista:
        print(el)
        
# miFuncionLista(['Chanchito', 'Feliz'])


def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i

nombres = concatenaNombres(['Chanchito', 'Feliz'])
print(nombres)
