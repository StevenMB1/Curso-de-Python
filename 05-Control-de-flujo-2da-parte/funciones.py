def miFuncion():
    print('Mi primera funcion!')
    
# miFuncion()

# def imprimeDato(nombre, apellido):
#     print('El nombre completo es:', nombre, apellido)
    
# imprimeDato('Chanchito', 'feliz')

def imprimeDato(*nombre):
    print('El nombre completo es:', nombre[1])
    
# imprimeDato('Chanchito', 'feliz', 'lala', 'lele')

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)
    
# nombreCompleto(nombre='Chanchito', apellido='Feliz')

def nombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])
    
nombreCompleto2(nombre='Chanchito', apellido='Feliz')

 