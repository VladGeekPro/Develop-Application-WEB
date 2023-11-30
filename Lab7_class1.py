from datetime import datetime 

class Departament:
  def __init__(self, nameDepartament, managerDepartament):
    self.nameDepartament = nameDepartament
    self.managerDepartament = managerDepartament

  def viewEmployeesList(self, employeeList):
    print("Employees list:")
    for employee in employeeList:
      print(f"- {employee} ")

class Employee(Departament):
  def __init__(self, nameEmployee, phone, bday, email, position):
    self.__nameEmployee = nameEmployee
    self.__phone = phone
    self.__bday = datetime.strptime(bday, "%Y-%m-%d")
    self.__email = email
    self.__position = position

  #Getter
  def get_nameEmployee(self):
    return self.__nameEmployee
  
  def get_phone(self):
    return self.__phone
  
  def get_bday(self):
    return self.__bday
  
  def get_email(self):
    return self.__email
  
  def get_position(self):
    return self.__position
  
  #Setter
  def set_nameEmployee(self, nameEmployee):
    self.__nameEmployee = nameEmployee
  
  def set_phone(self, phone):
    self.__phone = phone

  def set_bday(self, bday):
    self.__bday = datetime.strptime(bday, "%Y-%m-%d")

  def set_email(self, email):
    self.__email = email

  def set_position(self, position):
    self.__position = position

  #Property
  nameEmployee = property(get_nameEmployee, set_nameEmployee)
  phone = property(get_phone, set_phone)
  bday = property(get_bday, set_bday)
  email = property(get_email, set_email)
  position = property(get_position, set_position)  

  def calculateAge(self):
    today = datetime.now()
    age = today.year - self.__bday.year - ( (today.month, today.day) < (self.__bday.month, self.__bday.day) )
    return age
  
  def _calculateSalary(fun):
    def salaryEmployee(self, nmbrOfHour, hourlyPay):
      return fun(self, nmbrOfHour, hourlyPay)

    return salaryEmployee

  @_calculateSalary
  def hourlyEmployee(self, nmbrOfHour, hourlyPay):
    return nmbrOfHour * hourlyPay

