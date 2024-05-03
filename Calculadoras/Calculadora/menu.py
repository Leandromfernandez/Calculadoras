from funciones import *

def menu():
    primer_operando = None
    segundo_operando = None
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        
        opcion = pedir_entero('Ingrese la opción deseada. ', 'Error.Ingrese una opcón válida. ', 1, 5)
        
        if opcion == 1:
            primer_operando = pedir_entero('Ingrese el primer numero: ', 'Error. Ingrese un valor válido. ', -10000, 10000)
        elif opcion == 2:
            segundo_operando = pedir_entero('Ingrese el segundo numero: ', 'Error. Ingrese un valor válido. ', -10000, 10000)
        elif opcion == 3:
            if (primer_operando == None or segundo_operando == None):
                print('Error. Ingrese los dos operando.')
            else:
                resultado_suma = calcular_suma(primer_operando,segundo_operando)
                resultado_resta = calcular_resta(primer_operando, segundo_operando)
                resultado_division = calcular_division(primer_operando, segundo_operando)
                resultado_producto = calcular_producto(primer_operando, segundo_operando)
                resultado_potencia = calcular_potencia(primer_operando, segundo_operando)
                resultado_resto = calcular_resto(primer_operando, segundo_operando)
                
        elif opcion == 4:
            print(f'Los calculos con los numeros {primer_operando} y {segundo_operando}')
            print(f'La suma es: {resultado_suma}')
            print(f'La resta es: {resultado_resta}')            
            print(f'La division es: {resultado_division}')
            print(f'La multiplicación es: {resultado_producto}')
            print(f'El resultado de la potencia es: {resultado_potencia}')
            print(f'El resultado del resto es: {resultado_resto} ')
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")           
        
    
    
menu()
