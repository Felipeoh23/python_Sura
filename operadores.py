num1 = input(("Agregue el numero el primer numero"))

num2 = int(input("Agregue el segundo numero"))

sum = num1 + num2
rest = num1 - num2
mult = num1 * num2
div = num2 / num1
mod = num2 % num1

print(f"El resultado de la suma es {sum}")
print(f"El resultado de la Resta es {rest}")
print(f"El resultado de la Multiplicacion es {mult}")
print(f"El resultado de la Division es {div}")
print(f"El resultado de el modulo es {mod}")

greatest_tha = num1 > num2
less_than = num2 < num1

great_equal = num1 >= num2
less_equal = num2 <= num1
equal = num1 == num2
not_equal = num2 != num1

#Operadores logicos
#and or not

is_true = False and True
print(is_true)

is_false = False or True
print(is_false)

#Operadores de asigacion
# =, +=, -=, *=, /=

num1 = num1 + num2

num2 += num1

#jerarquia de operadores

"""
1. ()
2. ^, rad
3. *, /, %
4. +, -
5. >, <, >=, ==, !=
6. =, +=, -=, *=, /=
 




"""