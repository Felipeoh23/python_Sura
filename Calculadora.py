
init  = int(input("Presione 1 para Iniciar la app"))

sel = int(input("Seleccione una opción: "))
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")
if sel == 1:
    print("Suma")
    print(f"El resultado es {sum_result}") # type: ignore
elif sel == 2:
    print("Resta")
    print(f"El resultado es {rest_result}") # type: ignore
elif sel == 3:
    print("Multiplicar")
    print(f"El resultado es {mult_result}") # type: ignore
elif sel == 4:
    print("Dividir")
    print(f"El resultado es {div_result}") # type: ignore
else:
    print("Opción inválida")
    