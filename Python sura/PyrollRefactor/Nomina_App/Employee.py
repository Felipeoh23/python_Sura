class Employee:
    employee_id= None
    name_employee= None
    last_name_employee= None
    email= None
    password= None
    salary= None

    def __init__(self,employee_id, name_employee, last_name_employee, email, pasword, salary):
        self._employee_id = employee_id
        self._name_employee = name_employee
        self._last_name_employee = last_name_employee
        self._email = email
        self._password = pasword
        self._salary = salary

    @property
    def employee_id(self):
        return self._employee_id
    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id= emplyee_id



    @property
    def name_employee(self):
        return self._name_employee

    @name_employee.setter
    def name_employee(self,name_employee):
        self._name_employee= name_employee



    @property
    def last_name_employee(self):
        return self._last_name_employee

    @last_name_employee.setter
    def last_name_employee(self, last_name_employee):
        self._last_name_employee = last_name_employee


      @property
    def email(self):
          return self._email

      @email.setter
    def email(self,email):
          self._email=email



