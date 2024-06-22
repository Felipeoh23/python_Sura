#Elif

num1 = int(input("Agregue el primer número: "))
num2 = int(input("Agregue el segundo número: "))

sum_result = num1 + num2
rest_result = num1 - num2
mult_result = num1 * num2
div_result = num2 / num1
mod_result = num2 % num1 


print(f"El resultado de la suma es {sum_result}")
print(f"El resultado de la Resta es {rest_result}")
print(f"El resultado de la Multiplicación es {mult_result}")
print(f"El resultado de la División es {div_result}")
print(f"El resultado de el módulo es {mod_result}")

print("Seleccione una opción:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

sel = int(input("Seleccione una opción: "))


if sel == 1:
    print("Suma")
    print(f"El resultado es {sum_result}")
elif sel == 2:
    print("Resta")
    print(f"El resultado es {rest_result}")
elif sel == 3:
    print("Multiplicar")
    print(f"El resultado es {mult_result}")
elif sel == 4:
    print("Dividir")
    print(f"El resultado es {div_result}")
else:
    print("Opción inválida")
    

