from funciones import *
resultado_triangulo = None
resultado_rectangulo = None
valor_uno = None
valor_dos = None

while(True):
    menu()

    opcion = pedir_entero('Ingrese la opción deseada: ', 'Error. Ingrese una opción válida. ',1 , 8)

    match opcion:
        case 1:             
            valor_uno = pedir_flotante('Ingrese el primer valor: ', 'Error, ingrese el primer valor: ', -10000, 10000)
        case 2:            
            valor_dos = pedir_flotante('Ingrese el segudo valor: ', 'Error, ingrese el segundo valor: ', -10000, 10000)
        case 3:
            print("Calcular datos del triangulo rectangulo (Hipotenusa y angulos, area, perimetro)")
            resultado_triangulo = calcular_triangunlo(valor_uno, valor_dos)
            hipotenusa, area, perimetro = resultado_triangulo
        case 4:
            print("Calcular datos rectangulo (Diagonal, area, perimetro, relacion de aspecto)")
            resultado_rectangulo = calcular_rectangulo(valor_uno, valor_dos)
            area_rectangulo, perimetro_rectangulo, diagonal_rectangulo = resultado_rectangulo            
        case 5:
            print("Calcular datos cuadrado (Diagonal, area, perimetro)")
            resultado_cuadrado = calcular_cuadrado(valor_uno)
            area_cuadrado, perimetro_cuadrado, diagonal_cuadrado = resultado_cuadrado
        case 6:
            print("Imprimir datos guardados\n*")
            if resultado_triangulo is not None:
                print(f'*---Calculos triangulo---*\nHipotenusa: {hipotenusa}\nArea: {area}\nPerimetro: {perimetro}  \n*')
            else:
                print('*---Calculos rectangulo---*\nSIN DATOS')
            if resultado_rectangulo is not None:
                print(f'*---Calculos rectangulo---*\nArea del rectangulo: {area_rectangulo}\nPerimetro rectangulo: {perimetro_rectangulo}\nDiagonal: {diagonal_rectangulo}\n*')
            else:
                print('*---Calculos rectangulo---*\nSIN DATOS')
            if resultado_cuadrado is not None:
                print(f'*---Calculos cuadrado---*\nArea del cuadrado: {area_cuadrado}\nPerimetro cuadrado: {perimetro_cuadrado}\nDiagonal cuadrado: {diagonal_cuadrado}')
            else:
                print('*---Calculos cuadrado---*\nSIN DATOS')
        case 7:
            print("Borrar datos guardados")
            resultado_cuadrado = None
            resultado_rectangulo = None
            resultado_triangulo = None
            valor_uno = None
            valor_dos = None
            print('Datos borrados con exito. ')
        case 8:
            print("Saliendo... Hasta Pronto!. ")
            break