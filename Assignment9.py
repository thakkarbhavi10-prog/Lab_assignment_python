# Lab Assignment 1 (Employee → Manager Inheritance)
# class Employee:
#     def __init__(self):
#         self.name = ""
#         self.age = 0
#         self.salary = 0
#
#     def get_data(self):
#         self.name = input("Enter name: ")
#         self.age = int(input("Enter age: "))
#         self.salary = float(input("Enter salary: "))
#
#     def display_data(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Salary:", self.salary)
#
# class Manager(Employee):
#     def __init__(self):
#         super().__init__()
#         self.department = ""
#
#     def get_data(self):
#         super().get_data()
#         self.department = input("Enter department: ")
#
#     def display_data(self):
#         super().display_data()
#         print("Department:", self.department)
#
# # Processing 10 managers
# managers = []
#
# for i in range(10):
#     print(f"\nEnter details for Manager {i+1}")
#     m = Manager()
#     m.get_data()
#     managers.append(m)
#
# print("\n--- Manager Details ---")
# for i, m in enumerate(managers):
#     print(f"\nManager {i+1}")
#     m.display_data()


# Lab Assignment 2 (Library Management System)
# class Book:
#     def __init__(self, title):
#         self.title = title
#         self.is_issued = False
#
#
# class Member:
#     def __init__(self, name):
#         self.name = name
#         self.borrowed_books = []
#
#
# class Library:
#     def __init__(self):
#         self.books = []
#         self.members = []
#
#     def add_book(self, title):
#         self.books.append(Book(title))
#         print("Book added successfully!")
#
#     def add_member(self, name):
#         self.members.append(Member(name))
#         print("Member added successfully!")
#
#     def issue_book(self, member_name, book_title):
#         for book in self.books:
#             if book.title == book_title and not book.is_issued:
#                 for member in self.members:
#                     if member.name == member_name:
#                         book.is_issued = True
#                         member.borrowed_books.append(book_title)
#                         print("Book issued successfully!")
#                         return
#         print("Book not available!")
#
#     def return_book(self, member_name, book_title):
#         for member in self.members:
#             if member.name == member_name:
#                 if book_title in member.borrowed_books:
#                     member.borrowed_books.remove(book_title)
#                     for book in self.books:
#                         if book.title == book_title:
#                             book.is_issued = False
#                     print("Book returned successfully!")
#                     return
#         print("Invalid return!")
#
#     def display_books(self):
#         print("\nBooks in Library:")
#         for book in self.books:
#             status = "Issued" if book.is_issued else "Available"
#             print(book.title, "-", status)
#
#
# # Menu-driven system
# library = Library()
#
# while True:
#     print("\n1. Add Book")
#     print("2. Add Member")
#     print("3. Issue Book")
#     print("4. Return Book")
#     print("5. Display Books")
#     print("6. Exit")
#
#     choice = input("Enter choice: ")
#
#     if choice == '1':
#         title = input("Enter book title: ")
#         library.add_book(title)
#
#     elif choice == '2':
#         name = input("Enter member name: ")
#         library.add_member(name)
#
#     elif choice == '3':
#         member = input("Enter member name: ")
#         book = input("Enter book title: ")
#         library.issue_book(member, book)
#
#     elif choice == '4':
#         member = input("Enter member name: ")
#         book = input("Enter book title: ")
#         library.return_book(member, book)
#
#     elif choice == '5':
#         library.display_books()
#
#     elif choice == '6':
#         break
#
#     else:
#         print("Invalid choice!")