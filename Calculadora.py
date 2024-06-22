
init = int(input("Presione 1 para Iniciar la app: "))

while init == 1:
    sel = int(input("Seleccione una opción: \n"
                    "1. Sumar\n"
                    "2. Restar\n"
                    "3. Multiplicar\n"
                    "4. Dividir\n"
                    "5. Salir\n"))

    if sel == 1:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        sum_result = num1 + num2
        print("Suma")
        print(f"El resultado es {sum_result}")
    elif sel == 2:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        rest_result = num1 - num2
        print("Resta")
        print(f"El resultado es {rest_result}")
    elif sel == 3:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        mult_result = num1 * num2
        print("Multiplicar")
        print(f"El resultado es {mult_result}")
    elif sel == 4:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 != 0:
            div_result = num1 / num2
            print("Dividir")
            print(f"El resultado es {div_result}")
        else:
            print("Error: No se puede dividir entre cero")
    elif sel == 5:
        print("Saliendo de la app...")
        break
    else:
        print("Opción inválida")
    