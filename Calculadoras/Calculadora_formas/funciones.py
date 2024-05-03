def pedir_entero(mensaje, menjase_error, min, max):
    numero_entero = int(input(mensaje))
    while numero_entero > max or numero_entero < min:
        numero_entero = int(input(menjase_error))
    return numero_entero

def pedir_flotante(mensaje,mensaje_error, min, max):
    numero_flotante = float(input(mensaje))
    while numero_flotante < min or numero_flotante > max:
        numero_flotante = float(input(mensaje_error))
    return numero_flotante

def calcular_triangunlo(lado_uno, lado_dos):
    #lado_tres = float(input('Ingresa el lado_3: '))
    hipotenusa = (lado_uno ** 2) + (lado_dos ** 2)
    area = (lado_uno * lado_dos) / 2
    perimetro = lado_uno + lado_dos
    return hipotenusa, area, perimetro

def calcular_rectangulo(lado_uno, lado_dos):
    base = lado_uno
    altura = lado_dos
    hipotenusa = (base ** 2) + (altura ** 2)
    diagonal = (hipotenusa ** 2)
    area = (lado_uno * lado_dos)
    perimetro = 2 * (base + altura)

    return area, perimetro,diagonal

def calcular_cuadrado(lado_uno):
    area_cuadrado = (lado_uno * lado_uno)
    perimetro_cuadrado = lado_uno + lado_uno + lado_uno + lado_uno
    diagonal_cuadrado = lado_uno ** 2 + lado_uno **2
    diagonal_cuadrado = diagonal_cuadrado ** 2 
    
    return area_cuadrado, perimetro_cuadrado, diagonal_cuadrado
    
    


def menu():
    print('****************************************************************************************************')
    print('Bienvenido, Elija una opcioón para comenzar el programa. ')
    print('****************************************************************************************************')
    print('1.Ingrese el primer valor. ')
    print('2.Ingrese el segundo valor.')
    print('3.Calcular datos del triangulo rectangulo (Hipotenusa y angulos, area, perimetro).')
    print('4.Calcular datos rectangulo (Diagonal, area, perimetro, relacion de aspecto).')
    print('5.Calcular datos cuadrado (Diagonal, area, perimetro)").')
    print('6.Imprimir datos guardados.')
    print('7.Borrar datos. ')
    print('8.Salir. ')
    print('****************************************************************************************************\n')
