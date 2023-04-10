# a
def highest_number(num1, num2):
    if num1 > num2:
        return num1
    return num2


highest_number(13, 4)


# b
def lowest_number(numb1, numb2, numb3):
    if numb2 >= numb1 <= numb3:
        return numb1
    if numb1 >= numb2 <= numb3:
        return numb2
    return numb3


print(lowest_number(25, -14, 39))


# c
def module(argument):
    if argument < 0:
        return argument(-1)
    return argument


# d
def summ(argument1, argument2):
    print(argument1 + argument2)


summ(10, 12)


# e
def real_number(number):
    if number < 0:
        print('The number is negative')
    elif number > 0:
        print('The number is positive')
    else:
        print('The number is 0')


real_number(0)
