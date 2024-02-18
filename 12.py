def names(my_files):
    file = open(my_files, "a+")
    for i in range(3):
        file.write(input("Add a name: ") + "\n")
    file.close()

def print_names(my_files):
        file = open(my_files, "r+")
        for name in file.readlines():
            print(f"{name.strip()}")
        file.close()


names("names.txt")
print_names("names.txt")
