# Solicitar los números al usuario
num1 = int(input("Agregue el primer numero: "))  # Convertir a entero
num2 = int(input("Agregue el segundo numero: "))  # Convertir a entero

# Operaciones aritméticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else 'Indefinido'  # Evitar división por cero
modulo = num1 % num2 if num2 != 0 else 'Indefinido'  # Evitar módulo por cero

# Imprimir resultados de operaciones aritméticas
print(f"El resultado de la suma es {suma}")
print(f"El resultado de la resta es {resta}")
print(f"El resultado de la multiplicación es {multiplicacion}")
print(f"El resultado de la división es {division}")
print(f"El resultado del módulo es {modulo}")

# Comparaciones
mayor_que = num1 > num2
menor_que = num1 < num2
mayor_o_igual = num1 >= num2
menor_o_igual = num1 <= num2
igual = num1 == num2
diferente = num1 != num2

# Imprimir resultados de comparaciones
print(f"{num1} > {num2} : {mayor_que}")
print(f"{num1} < {num2} : {menor_que}")
print(f"{num1} >= {num2} : {mayor_o_igual}")
print(f"{num1} <= {num2} : {menor_o_igual}")
print(f"{num1} == {num2} : {igual}")
print(f"{num1} != {num2} : {diferente}")

# Operadores lógicos
is_true = False and True
print(f"False and True es {is_true}")

is_false = False or True
print(f"False or True es {is_false}")

# Operadores de asignación
num1 += num2
print(f"Nuevo valor de num1 (num1 += num2): {num1}")

num2 += num1
print(f"Nuevo valor de num2 (num2 += num1): {num2}")
