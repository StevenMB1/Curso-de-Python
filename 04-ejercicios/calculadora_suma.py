primero = input('Ingrese un numero: ')

try:
    primero = int(primero)
except:
    primero = 'chanchito feliz'

segundo = input('Ingrese un segundo numero: ')

try:
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'
    
if primero == 'chanchito feliz' or segundo == 'chanchito feliz':
    print('Ingresaste mal un dato, prueba de nuevo solo con numeros')
else:
    print(primero + segundo)


