from payroll_app.User import User


class Costumer(User):

    type = None
    points = None

    def _init_(self, employee_id, name_employee, last_name_employee, email, password, type, points):
        super()._init_(employee_id, name_employee, last_name_employee, email, password)
        self._type = type
        self._points = points

    def __init__(self, employee_id, name_employee, last_name_employee, email, password):
        super().__init__(employee_id, name_employee, last_name_employee, email, password)
        self.appent = None

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self.type = type

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        self.points = points

    #costumers = {}

    def create_user(self):
        super().create_user()
        type = input("Tipo de cliente: ")
        points = int(input("Puntos: "))
        [self._employee_id]=  {"nombre": self._name_employee, "Apellido": self._last_name_employee, "email": self._email, "contraseña": self._password}

    def list_costumers(self):
        for item in self.costumer():
            print(item)