#Task 1 (a)
# Lab Assignment - 1 (Tuple Operations)

# Taking input from user
# numbers = tuple(map(int, input("Enter integers separated by space: ").split()))

# a) Total number of items
# print("Total number of items:", len(numbers))

# b) Last item in the tuple
# print("Last item:", numbers[-1])

# c) Elements in reverse order
# print("Tuple in reverse order:", numbers[::-1])

# d) Check if 5 is present
# if 5 in numbers:
#     print("5 is present in the tuple")
# else:
#     print("5 is NOT present in the tuple")

# e) Remove first and last items
# if len(numbers) > 2:
#     new_tuple = numbers[1:-1]
#     print("Tuple after removing first and last items:", new_tuple)
# else:
#     print("Not enough elements to remove first and last items")


# Lab Assignment - 2 (Price Analysis using Tuple)

prices = tuple(map(float, input("Enter prices of sold items: ").split()))

# a) Total number of items sold
# print("Total items sold:", len(prices))

# b) Cheapest item price
# print("Cheapest item price:", min(prices))

# c) Costliest item price
# print("Costliest item price:", max(prices))

# d) Prices in ascending order
# print("Prices in ascending order:", tuple(sorted(prices)))

# e) Number of costliest items sold
# costliest_count = prices.count(max(prices))
# print("Number of costliest items sold:", costliest_count)