
# *************day-3***************
def calculate_tax(salary):
    if salary < 30000:
        tax = 0
    elif salary <= 60000:
        tax = 0.1 * salary
    else:
        tax = 0.2 * salary
    return tax
  
def calculate_net_salary(salary, tax):
    net_salary = salary - tax
    return net_salary


def save_tax_record():
    name= input("Enter your name:")
    salary = int(input("Enter your salary:"))
    tax = calculate_tax(salary)
    net_salary=calculate_net_salary(salary,tax)
    file = open("tax_records.txt", "a")   # "a" means append (add new data)
    file.write(f"Name: {name}, Salary: {salary}, Tax: {tax}\n")
    file.close()
    