# and solo se cumple si las 2 intrucciones son verdaderas.
if 2 < 5 and  3 > 2:
    print('ambas devuelven true')

if 2 < 5 and  3 < 2:
    print('hay una falsa, esto no se mostrara')
    
# "or", si una de las dos condiciones devuelve true, entonces todos se evaluan true. si ambas son falsas no se ejecuta

if 1 < 0 or 1 > 0: # si una condicion evalua en true se ejecuta la instrucción.
    print('una de las dos condiciones devolvio true')
    
if 1 < 0 or 1 < 0: # si ambas condiciones son falsas entonces no se ejecuta.
    print('Si ambas condiciones evaluan en false no se ejecuta esto.!')