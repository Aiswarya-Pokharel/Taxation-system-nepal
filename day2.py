# employee_list = []
# tax_list = []

for i in range(1, 6):
    print("\nEntering details for Employee:", i)
    name = input("Enter employee name: ")
    normal_salary = int(input("Enter your monthly salary: "))
    tax_salary = int(input("Enter your exact salary: "))
    
    tax_percent = ((normal_salary - tax_salary) / normal_salary) * 100

