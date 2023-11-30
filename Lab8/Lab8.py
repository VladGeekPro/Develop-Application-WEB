from  Lab8_class import Employee, Departament, HourlyEmployee, SalaryEmployee

  
try:
  emp1 = HourlyEmployee(10, 20, "King", "068815643", "2022-11-25", "king@gmail.com", "CEO")
  emp2 = SalaryEmployee(5000, "Prince", "068815634", "2020-03-14", "prince@gmail.com", "System Admin")

  print(f"{emp1.nameEmployee}'s salary: {emp1.calculateSalary()}$")
  print(f"{emp2.nameEmployee}'s salary: {emp2.calculateSalary()}$")
except Exception as e:
  print(f"No results for {e}")
