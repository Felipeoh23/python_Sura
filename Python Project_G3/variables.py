
"""
name = "Pedro"
lastName: str = "Castro"
number: int = "dos"

print(type(number))

note= 4.5
print(type(note))

age = 29
print(type(age))

isActive = True


print(type(isActive))

ages = [15, 19,29,21, 30]

print(type(ages))

week_days = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
print(type(week_days))

user = {"Name": "Maria", "Age": 19 }
print(type(user))

notes = {4.5, 2.8, 4.0, 3.5}
print(type(notes))
"""
from unittest import result


num1 = int(input("Agregue el numero 1 y sumelo con el 2"))
sum = num1 + 2
#print("El Resultado Es", sum)

print(f"El resultado es{sum}")

def sum2(num1):
    num2 = 2
    return num1 + num2
    result = sum2(num1)

print(f"El resultado de la suma es {result}")


