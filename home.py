
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
    file = open("tax_records.txt", "a")   # "a" means append (add new data)
    for i in range(3):
        name= input("Enter employee name:")
        salary = int(input("Enter employee salary:"))
        tax = calculate_tax(salary)
        net_salary=calculate_net_salary(salary,tax)
    
        file.write(f"{name}, {salary}, {tax}, {net_salary}\n")
    file.close()
    
def read_tax_records():
    file = open("tax_records.txt", "r")
    data = file.read()

    print("Tax Records:")
    print("Name\t Salary\t Tax\t Net Salary")

    for line in data.splitlines():
        print(line.replace(",", "\t"))

    file.close()

if __name__ == "__main__":
    save_tax_record()
    read_tax_records()