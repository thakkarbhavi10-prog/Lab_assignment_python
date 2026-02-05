#Practical 1-Lab Assignment 1
# Employee Salary Program
# name = input("Enter employee name: ")
# emp_id = input("Enter employee ID: ")
# dept = input("Enter department: ")
# basic = float(input("Enter basic salary: "))
#
# da = 0.92 * basic
# hra = 0.58 * basic
# ta = 0.30 * basic
# lic = 500
#
# gross_salary = basic + da + hra + ta

# print("\n--- Employee Details ---")
# print("Name:", name)
# print("Employee ID:", emp_id)
# print("Department:", dept)
# print("Basic Salary:", basic)
# print("Net Salary:", net_salary)

#Practical 1-Lab Assignment 2
# Vendor Details Program
# name = input("Enter vendor name: ")
# year = int(input("Enter year of association: "))
# contact = input("Enter contact number: ")
# email = input("Enter email ID: ")
#
# total_purchase = 0
#
# for i in range(1, 13):
#     amount = float(input(f"Enter purchase amount for month {i}: "))
#     total_purchase += amount
#
# print("\n--- Vendor Details ---")
# print("Vendor Name:", name)
# print("Year of Association:", year)
# print("Contact Number:", contact)
# print("Email ID:", email)
# print("Annual Purchase Amount:", total_purchase)

#Practical 2-Lab Assignment 1
# Ohm's Law Program
# voltage = float(input("Enter voltage (V): "))
# resistance = float(input("Enter resistance (R): "))
#
# current = voltage / resistance
# print("Current:", current, "A")
#
# if current < 0.5:
#     print("Low current")
# elif current <= 2:
#     print("Normal current")
# else:
#     print("High current")

#Practical 2-Lab Assignment 2
# Steel Grade Program
hardness = int(input("Enter hardness: "))
carbon = float(input("Enter carbon content: "))
tensile = int(input("Enter tensile strength: "))

cond1 = hardness > 50
cond2 = carbon < 0.7
cond3 = tensile > 5600

if cond1 and cond2 and cond3:
    grade = 10
elif cond1 and cond2:
    grade = 9
elif cond2 and cond3:
    grade = 8
elif cond1 and cond3:
    grade = 7
elif cond1 or cond2 or cond3:
    grade = 6
else:
    grade = 5

print("Grade of steel:", grade)

