
# *************day-2***************

salary = int(input("Enter your salary: "))
if salary <30000:
  tax = 0
elif  salary<=6000:
  tax = 0.1*salary
else:
  tax = 0.2*salary
net_salary = salary - tax
print("Salary: ",salary)
print("Tax: ",tax)
print("Net Salary: ",net_salary)

##day 3##

def save_tax_record(name, salary, tax):
    file = open("tax_records.txt", "a")   # "a" means append (add new data)
    file.write(f"Name: {name}, Salary: {salary}, Tax: {tax}\n")
    file.close()
