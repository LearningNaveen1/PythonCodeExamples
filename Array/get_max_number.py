'''
    Finding maximum number in array
'''


lst = []



'''
    Preparing a method for taking values from user
'''
def get_input():
    n = int(input("Enter a number for list: "))
    for i in range(0,n):
        temp = int(input())
        lst.append(temp)

'''
    Method for checking maximum number
'''
def check_maximum(lst):
    max = lst[0]
    for i in range(len(lst)):
        if max < lst[i]:
            max = lst[i]
    print("Max number is " , max)

get_input()
check_maximum(lst)