#************ Task-3-Anuja *************
for i in range(1, 6):
# ************* Task-1-Aishwarya ***************    
    print("\nEntering details for Employee:", i)
    name = input("Enter employee name: ")
    salary = int(input("Enter your exact salary: "))
# ************* Task-2-Anuska ***************
    if salary <30000:
        tax = 0
    elif  salary<=6000:
        tax = 0.1*salary
    else:
        tax = 0.2*salary

# ************* Task-4-Asmita ***************    

    print("\nEmployee Name:", name)
    print("Tax Amount:", tax)
    print("Normal Salary:", salary)
    print("Exact Salary:", salary-tax)
        
    
    

