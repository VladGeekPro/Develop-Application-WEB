from  Lab7_class1 import Employee
#from  Lab7_class2 import Employee

  
try:
  emp1 = Employee("King", "068815643", "2022-11-25", "king@gmail.com", "CEO")
  print(f"Name: {emp1.nameEmployee}\nPhone: {emp1.phone}\nBirthday: {emp1.bday}\nEmail: {emp1.email}\nPosition: {emp1.position}")
  print(f"The employee age is = {emp1.calculateAge()}")

  emp1.set_nameEmployee("Vlad")
  print(f"New employee name is {emp1.nameEmployee}")

  # emp1.bday = "2023-08-01"
  # print(f"New employee bday is {emp1.bday}")

  print(f"The employee salary with 10$ for 10H = {emp1.hourlyEmployee(10, 10)}$")

except Exception as e:
  print(f"No results for {e}")
