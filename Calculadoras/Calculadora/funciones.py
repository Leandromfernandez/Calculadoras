def pedir_entero(mensaje, menjase_error, min, max):
    numero_entero = int(input(mensaje))
    while numero_entero > max or numero_entero < min:
        numero_entero = int(input(menjase_error))
    return numero_entero

def calcular_suma(num_a, num_b):
    return num_a + num_b

def calcular_resta(num_a, num_b):
    return num_a - num_b

def calcular_division(num_a, num_b):
    if num_a ==0 or num_b == 0:
        return print('No se puede dividir por 0.')
    else:
        return num_a / num_b

def calcular_producto(num_a, num_b):
    return num_a * num_b

def calcular_potencia(num_a, num_b):
    return num_a ** num_b

def calcular_resto(num_a, num_b):
    if num_a ==0 or num_b == 0:
        return print('No se puede realizar la operacion de resto. ')
    else: 
        return num_a % num_b