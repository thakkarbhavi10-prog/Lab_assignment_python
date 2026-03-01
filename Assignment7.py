# Lab Assignment - 1
# Menu Driven Calculator using Functions

# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Division by zero not allowed"
#
# def modulus(a, b):
#     return a % b
#
# while True:
#     print("\n--- CALC MENU ---")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Modulus")
#     print("6. Exit")
#
#     choice = int(input("Enter your choice: "))
#
#     if choice == 6:
#         print("Calculator Closed")
#         break
#
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#
#     if choice == 1:
#         print("Result:", add(a, b))
#     elif choice == 2:
#         print("Result:", subtract(a, b))
#     elif choice == 3:
#         print("Result:", multiply(a, b))
#     elif choice == 4:
#         print("Result:", divide(a, b))
#     elif choice == 5:
#         print("Result:", modulus(a, b))
#     else:
#         print("Invalid choice")

# Lab Assignment - 2
# Bank Account Menu Driven Program using Functions

# balance = 0
#
# def display_balance():
#     print("Current Balance:", balance)
#
# def deposit(amount):
#     global balance
#     balance += amount
#     print("Amount Deposited Successfully")
#
# def withdraw(amount):
#     global balance
#     if amount <= balance:
#         balance -= amount
#         print("Amount Withdrawn Successfully")
#     else:
#         print("Insufficient Balance")
#
# while True:
#     print("\n--- BANK MENU ---")
#     print("1. Display Balance")
#     print("2. Deposit Amount")
#     print("3. Withdraw Amount")
#     print("4. Exit")
#
#     choice = int(input("Enter your choice: "))
#
#     if choice == 1:
#         display_balance()
#     elif choice == 2:
#         amt = int(input("Enter amount to deposit: "))
#         deposit(amt)
#     elif choice == 3:
#         amt = int(input("Enter amount to withdraw: "))
#         withdraw(amt)
#     elif choice == 4:
#         print("Thank you for using Bank Application")
#         break
#     else:
#         print("Invalid choice")
#
