import math
import sys

def radtopi(num):
    return num*math.pi/180
def pitorad(num):
    return num*180/math.pi

def sortalist(numbers):
    sorted_list = []
    order = input("press 1 for ascending order and 2 for descending order: ")
    #did not work I still broke my head on this
    # if int(order) == 1:
    #     for i in range(length):
    #         tempmax = numbers[i]
    #         for j in range(length):
    #             if max(tempmax, numbers[j]) == numbers[j]:
    #                 tempmax = numbers[j]
    #             elif max(tempmax, numbers[j]) == numbers[i]:
    #                 tempmax = numbers[i]
    #         sorted_list.append(tempmax)
    #         numbers.remove(tempmax)
    #         length -= length
    #         if tempmax == numbers[i]:
    #
    #             tempmax =-sys.maxsize
    #
    #         if tempmax == numbers[j]:
    #
    #             tempmax = -sys.maxsize
    #
    # return sorted_list
    while numbers:
        if not (order == '1' or order == '2'):
            order = input("Wrong input! press 1 for ascending order and 2 for descending order: ")
        if order == '1':
            tempmax = max(numbers)
            sorted_list.append(tempmax)
            numbers.remove(tempmax)
        if order == '2':
            tempmin = min(numbers)
            sorted_list.append(tempmin)
            numbers.remove(tempmin)
    return sorted_list

def dec2bin(num):
    if num> 1024:
        return "due to CPU limitation Im Unable to process this try again with numbers smaller than 1024"
    



