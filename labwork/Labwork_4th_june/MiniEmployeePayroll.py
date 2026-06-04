name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

hra = basic_salary * 0.20
da = basic_salary * 0.10
pf = basic_salary * 0.12

gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf

print("\nEmployee Name:", name)
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("PF Deduction:", pf)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)

if net_salary > 50000:
    print("Grade: Senior Grade")
elif net_salary > 30000:
    print("Grade: Mid Grade")
else:
    print("Grade: Junior Grade")