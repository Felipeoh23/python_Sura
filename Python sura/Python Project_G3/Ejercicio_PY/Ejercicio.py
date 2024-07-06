class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        print(f"El saldo actual es: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Has depositado ${amount:.2f}. El nuevo saldo es: ${self.balance:.2f}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Has retirado ${amount:.2f}. El nuevo saldo es: ${self.balance:.2f}")
            else:
                print("Fondos insuficientes.")
        else:
            print("La cantidad a retirar debe ser positiva.")

    def run(self):
        while True:
            print("\nBienvenido al cajero automático")
            print("Por favor, selecciona una opción:")
            print("1. Consultar saldo")
            print("2. Depositar dinero")
            print("3. Retirar dinero")
            print("4. Salir")

            option = input("Introduce el número de la opción que deseas: ")

            if option == '1':
                self.check_balance()
            elif option == '2':
                amount = float(input("Introduce la cantidad a depositar: "))
                self.deposit(amount)
            elif option == '3':
                amount = float(input("Introduce la cantidad a retirar: "))
                self.withdraw(amount)
            elif option == '4':
                print("Gracias por usar el cajero automático. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")

# instancia del cajero
atm = ATM(initial_balance=10000)
atm.run()
