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
  @property
  def nameEmployee(self):
    return self.__nameEmployee
  
  @property
  def phone(self):
    return self.__phone
  
  @property
  def bday(self):
    return self.__bday
  
  @property
  def email(self):
    return self.__email
  
  @property
  def position(self):
    return self.__position
  
  #Setter
  @nameEmployee.setter
  def nameEmployee(self, nameEmployee):
    self.__nameEmployee = nameEmployee
  
  @phone.setter
  def phone(self, phone):
    self.__phone = phone

  @bday.setter
  def bday(self, bday):
    self.__bday = datetime.strptime(bday, "%Y-%m-%d")

  @email.setter
  def email(self, email):
    self.__email = email

  @position.setter
  def position(self, position):
    self.__position = position
  

  def calculateAge(self):
    today = datetime.now()
    age = today.year - self.__bday.year - ( (today.month, today.day) < (self.__bday.month, self.__bday.day) )
    return age
  
  def _calculateSalary():
    pass
  
class HourlyEmployee(Employee):
  def __init__(self, nmbrOfHour, hourlyPay, nameEmployee, phone, bday, email, position):
    super().__init__(nameEmployee, phone, bday, email, position)
    self.__nmbrOfHour = nmbrOfHour
    self.__hourlyPay  = hourlyPay
  
  def calculateSalary(self):
    return self.__nmbrOfHour * self.__hourlyPay

class SalaryEmployee(Employee):
  def __init__(self, salary, nameEmployee, phone, bday, email, position):
    super().__init__(nameEmployee, phone, bday, email, position)
    self.__salary = salary
  
  def calculateSalary(self):
    return self.__salary

