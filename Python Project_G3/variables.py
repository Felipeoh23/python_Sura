# Variables y tipos de datos
name = "Pedro"
lastName: str = "Castro"
number: str = "dos"  # Cambiado a str ya que "dos" no es un número

print(type(number))  # str

note = 4.5
print(type(note))  # float

age = 29
print(type(age))  # int

isActive = True
print(type(isActive))  # bool

ages = [15, 19, 29, 21, 30]
print(type(ages))  # list

week_days = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
print(type(week_days))  # tuple

user = {"Name": "Maria", "Age": 19}
print(type(user))  # dict

notes = {4.5, 2.8, 4.0, 3.5}
print(type(notes))  # set

# Función para sumar 2 a un número dado
def sum2(num1: int) -> int:
    num2 = 2
    return num1 + num2

# Solicitar número al usuario y realizar la suma
try:
    num1 = int(input("Agregue el numero 1 y súmelo con el 2: "))
    result = sum2(num1)
    print(f"El resultado es {result}")
except ValueError:
    print("Por favor, ingrese un número válido.")




