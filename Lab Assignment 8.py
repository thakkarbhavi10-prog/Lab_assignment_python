 # Lab Assignment 1 (File → Uppercase Copy)
# Read file and write uppercase content to new file

# source = input("Enter source file name: ")
# destination = input("Enter destination file name: ")
#
# with open(source, 'r') as f:
#     content = f.read()
#
# with open(destination, 'w') as f:
#     f.write(content.upper())
#
# print("File copied with uppercase content successfully!")


# Lab Assignment 2 (Copy Python file without comments)
# source = input("Enter source Python file: ")
# destination = input("Enter destination file: ")
#
# with open(source, 'r') as f:
#     lines = f.readlines()
#
# clean_lines = []
#
# for line in lines:
#     line = line.strip()
#     if not line.startswith("#") and line != "":
#         clean_lines.append(line)
#
# with open(destination, 'w') as f:
#     for line in clean_lines:
#         f.write(line + "\n")
#
# # Display both files
# print("\n--- Source File Content ---")
# with open(source, 'r') as f:
#     print(f.read())
#
# print("\n--- Destination File Content (No Comments) ---")
# with open(destination, 'r') as f:
#     print(f.read())