
number = 0
def get_input_from_user():
    return int(input("Enter Value : "))
#    number = int(input("Enter the number"))



# In below mentioned loop we can't use parameter in range function, so better to use while loop
# def check_perfect_square():
#     for i in range(1,number,i*i):
#         if((number % i == 0) and ( number / i == i)):
#             return True
#
#     return False

def check_perfect_square(number):
    i = 1
    while (i*i <= number):
        if ((number % i == 0) and (number / i == i)):
            return True
        i = i + 1
    return False

number = get_input_from_user()
print(check_perfect_square(number))