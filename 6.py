for i in range(5):
    print("counter is :" + (str(i + 1)))
else:
    print("finished")
class_mates = ["maxim", "yoni", "gilad", "oren"]
for name in class_mates:
    print(name)

for i in range(len(class_mates)):
    print(class_mates[i])

your_name = input("enter you name ")

while your_name != "shahar":
    print("you are not shahar")
    if your_name == "david":
        print("omg")
        break
    elif your_name == "omer":
        print("wow")
        your_name = input("enter you name ")
        continue
    your_name = input("enter you name ")
else:
    print("your name is :" + your_name)
