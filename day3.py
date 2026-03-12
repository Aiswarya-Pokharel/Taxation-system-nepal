def calculate_tax(salary):
    if salary < 30000:
        tax = 0
    elif salary <= 60000:
        tax = 0.1 * salary
    else:
        tax = 0.2 * salary
    return tax