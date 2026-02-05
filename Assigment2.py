#Task1
#1
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
#2
# for i in range(1, 6):
#     for j in range(i):
#         print(i, end="")
#     print()
#3
# for i in range(1, 6):
#     for j in range(i, 0, -1):
#         print(j, end="")
#     print()
#4
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j % 2, end="")
#     print()
#5
# num = 2
# for i in range(1, 5):
#     for j in range(i):
#         print(num, end=" ")
#         num += 2
#     print()
#6
# for i in range(1, 6):
#     print("*" * i)

#Task2
#1
# for i in range(1, 6):
#     ch = 'A'
#     for j in range(i):
#         print(chr(ord(ch) + j), end="")
#     print()
#2
# symbols = ['*', '#']
#
# for i in range(1, 6):
#     for j in range(i):
#         print(symbols[j % 2], end=" ")
#     print()
#3
# letters = ['p', 'y', 't', 'h', 'o']
# for i in range(5):
#     for j in range(i + 1):
#         print(letters[i], end="")
#     print()
#4
# word = "python"
# for i in range(1, len(word) + 1):
#     for j in range(i):
#         print(word[j], end="")
#     print()

#Task3
# n = int(input("Enter n: "))
#
# if 1 <= n <= 150:
#     for i in range(1, n + 1):
#         print(i, end="")
# else:
#     print("Invalid input")

#Task4
# rows = 5
#
# for i in range(rows):
#     print(" " * i + "* " * (rows - i))

#Task5
# rows = 5
# for i in range(1, rows + 1):
#     # print leading spaces
#     print(" " * (rows - i) * 2, end="")
#
#     # print stars
#     for j in range(2 * i - 1):
#         print("* ", end="")
#     print()

#Task6
# Upper part (increasing)
# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
#     print()
#
# # Lower part (decreasing)
# for i in range(4, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

#Task7
# Input using while loop
# while True:
#     start = int(input("Enter start number: "))
#     end = int(input("Enter end number: "))
#     if start > 1 and end > start:
#         break
#     print("Invalid input. Try again.")
#
# print("Prime numbers are:")
#
# for num in range(start, end + 1):
#     if num > 1:
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num, end=" ")

