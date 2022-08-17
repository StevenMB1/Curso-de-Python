#TODO Calculadora que suma.

# primero = input('Ingrese primer numero: ')

# try:
#     primero = int(primero)
# except:
#     primero = ''
    

# segundo = input('Ingrese segundo numero: ')

# try:
#     segundo = int(segundo)
# except:
#     segundo = ''
    
# if primero == '' or segundo == '':
#     print('Ingresaste mal un dato, prueba de nuevo solo con numeros')
# else:
#     print(primero + segundo)


#TODO Moviendo la validacion

# primero = input('Ingrese primer numero: ')

# try:
#     primero = int(primero)
# except:
#     primero = ''
    
# if primero == '':
#     print('El valor ingresado no es un entero')
#     exit()

# segundo = input('Ingrese segundo numero: ')

# try:
#     segundo = int(segundo)
# except:
#     segundo = ''
    
# if segundo == '':
#     print('El valor ingresado no es un entero')
#     exit()

# print(primero + segundo)


#TODO Agregando mas operaciones

primero = input('Ingrese primer numero: ')

try:
    primero = int(primero)
except:
    primero = ''
    
if primero == '':
    print('El valor ingresado no es un entero')
    exit()

segundo = input('Ingrese segundo numero: ')

try:
    segundo = int(segundo)
except:
    segundo = ''
    
if segundo == '':
    print('El valor ingresado no es un entero')
    exit()

simbolo = input('Ingrese operacion: ')

if simbolo == '+':
    print('Suma:', primero + segundo)
elif simbolo == '-':
    print('Resta:', primero - segundo)
elif simbolo == '*':
    print('Multiplicacion', primero * segundo)
elif simbolo == '/':
    print('Division', primero / segundo)
else:
    print('El simbolo ingresado no es valido')
    
