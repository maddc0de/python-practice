from employeesArray import employees

# 1. Print the name of the person who has the highest salary at the company
def find_highest_paid_employee(employeeList):
  highest_salary = 0
  highest_paid_employee = ""

  # loop through each element of the array to access each object
  for employee in employeeList:
    # access the value of each employee's salary then compare the values
    if employee.get('salary') > highest_salary:
      highest_salary = employee.get('salary')
      highest_paid_employee = f"{employee.get('first_name')} {employee.get('last_name')}"
    else:
      pass
  
  print(f"Employee with the highest salary is: {highest_paid_employee}")
  
find_highest_paid_employee(employees)


# 2. Print the combined years of experience of all employees at the company.
def calculate_total_years_of_experience(employeeList):
  salaries = [employee.get('years_of_experience') for employee in employeeList]
  total_years = sum(salaries)

  print(f"total years of experience of all employee is: {total_years}")

calculate_total_years_of_experience(employees)


# 3. Some people don't have an email address - collect their details into a new list!
def find_employees_without_email(employeeList):
  employees_without_email = []

  for employee in employeeList:
    if employee.get('email') == None:
      employees_without_email.append(employee)
  
  print(f"employees without an email address: {employees_without_email}")

find_employees_without_email(employees)


# 4. Which one costs more for the company - Product department salaries or Business department salaries?
def find_department_with_most_costs(employeeList):
  product_total_cost = 0
  business_total_cost = 0

  for employee in employeeList:
    if employee.get('department') == "Product":
      product_total_cost += employee.get('salary')
    elif employee.get('department') == "Business":
      business_total_cost += employee.get('salary')
    else:
      pass
  
  if product_total_cost > business_total_cost:
    print(f"Product department costs more by: {product_total_cost - business_total_cost}")
  elif business_total_cost > product_total_cost:
    print(f"Business department costs more by: {business_total_cost - product_total_cost}")

find_department_with_most_costs(employees)
