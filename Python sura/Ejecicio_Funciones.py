empleados = []

def registrar_empleado():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    cargo = input("Ingrese el cargo: ")
    salario = float(input("Ingrese el salario: "))
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")

    empleado = {
        'nombre': nombre,
        'apellido': apellido,
        'cargo': cargo,
        'salario': salario,
        'usuario': usuario,
        'contraseña': contraseña
    }

    empleados.append(empleado)

def obtener_salario(empleado):
    return empleado['salario']

def obtener_descuento_salud(empleado):
    return obtener_salario(empleado) * 0.04

def obtener_descuento_pension(empleado):
    return obtener_salario(empleado) * 0.04

def obtener_salario_neto(empleado):
    return obtener_salario(empleado) - obtener_descuento_salud(empleado) - obtener_descuento_pension(empleado)

def iniciar_sesion():
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")

    for empleado in empleados:
        if empleado['usuario'] == usuario and empleado['contraseña'] == contraseña:
            return empleado

    return None

def imprimir_datos_empleado(empleado):
    print(f"Nombre: {empleado['nombre']} {empleado['apellido']}")
    print(f"Cargo: {empleado['cargo']}")
    print(f"Salario: {obtener_salario(empleado)}")
    print(f"Descuento Salud: {obtener_descuento_salud(empleado)}")
    print(f"Descuento Pension: {obtener_descuento_pension(empleado)}")
    print(f"Salario Neto: {obtener_salario_neto(empleado)}")

def menu():
    while True:
        print("1. Registrar Empleado")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            registrar_empleado()
        elif opcion == 2:
            empleado = iniciar_sesion()
            if empleado is not None:
                imprimir_datos_empleado(empleado)
            else:
                print("Credenciales inválidas")
        elif opcion == 3:
            break
        else:
            print("Opción inválida")

menu()