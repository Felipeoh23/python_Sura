
"""salary= int(input("Ingrese el salario"))

def calculateNetSalary(salary):
 healtDiscount = salary *0.04
 pensionDiscount = salary *0.04

 netSalary = salary - healtDiscount - pensionDiscount

 return netSalary
 """
def calculate_net_salary(salary, health_discount_rate, pension_discount_rate):
    health_discount = salary * health_discount_rate
    pension_discount = salary * pension_discount_rate

    net_salary = salary - health_discount - pension_discount

    return net_salary

salary = int(input("Ingrese el salario: "))
health_discount_rate = float(input("Ingrese la tasa de descuento de salud (0.04 para 4%): "))
pension_discount_rate = float(input("Ingrese la tasa de descuento de pensión (0.04 para 4%): "))


net_salary = calculate_net_salary(salary, health_discount_rate, pension_discount_rate)

print("El salario neto es:", net_salary)

