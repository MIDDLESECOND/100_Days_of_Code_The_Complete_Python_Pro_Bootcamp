file = open("example_file.txt")
content = file.read()
print(content)
file.close()
# need to close since opened file took resources


with open("example_file.txt") as file:
    content = file.read()
    print(content)
    # for with we do not need to care about closing



# can also write the file, need to change the mode to w for write mode, r is for read-only
with open("example_file.txt", mode = 'w') as file:
    file.write("New text.")

# mode = a will add the information (append)
with open("example_file.txt", mode = 'a') as file:
    file.write("\nNew text 2.")
    # \n add a new line


# if the file does not exist, it will create it for u
with open("example_file_2.txt", mode = 'w') as file:
    file.write("Amami Tsubasa")