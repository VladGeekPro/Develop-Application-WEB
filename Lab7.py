from  Lab7_class1 import Employee, Departament
#from  Lab7_class2 import Employee

  
try:
  dep1 = Departament("It control", "Vladislav Juracovschi")

  emp1 = Employee("King", "068815643", "2022-11-25", "king@gmail.com", "CEO")
  print(f"Name: {emp1.nameEmployee}\nPhone: {emp1.phone}\nBirthday: {emp1.bday}\nEmail: {emp1.email}\nPosition: {emp1.position}")
  print(f"The employee age is = {emp1.calculateAge()}")

  emp2 = Employee("Dan", "068815634", "2020-03-14", "prince@gmail.com", "System Admin")
  emp3 = Employee("Ana", "079015638", "2020-03-14", "and@gmail.com", "HR")
  
  emp1.set_nameEmployee("Vlad")
  print(f"New employee name is {emp1.nameEmployee}")

  # emp1.bday = "2023-08-01"
  # print(f"New employee bday is {emp1.bday}")

  print(f"The employee salary with 10$ for 10H = {emp1.hourlyEmployee(10, 10)}$")
  employeeList = []
  employeeList = [emp1.nameEmployee, emp2.nameEmployee, emp3.nameEmployee ]
  dep1.viewEmployeesList(employeeList)

  
except Exception as e:
  print(f"No results for {e}")
