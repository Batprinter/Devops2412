import requests
try:
    requests.get("rhehreh:bnfej")
except BaseException as e:
    print("ruh oh")
    print(e.args)
try:
    a = int(input("enter num: "))
    b = int(input("enter num: "))

    print(a / b)

except ValueError:
    print("enter a number")
except ZeroDivisionError:
    print("can't divide by 0")
except BaseException as e:
    print("noo")

