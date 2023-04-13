# a

def positional_arguments(*args):
    """Function return list of an unspecified number of arguments"""
    return list(set(args))


print(positional_arguments('Bob', 'Pete', False, None, 5, 4, 5))

#assert list(positional_arguments()) == ['Bob', 'Pete', False, None, 5, 4, 5]


# b


def named_arguments(user_type='Student', **kwargs):
    print(len(kwargs))
    #print(dict(kwargs[user_type]))


named_arguments(user_name='Bob', user_age=23, user_sex='male')


# c


def mixed_arguments(positional1, positional2, /, mixed, named, five=5, six=6):
    pass


mixed_arguments(1, 2, 3, named=4, five=5, six=6)


# d
# def number1(num1=int):
#     return number2()
#
#
# def number2(num2=int):
#     return num1*num2
#
# print(number1(num1=2, num2=3))


# e


def square(num):
    print('*' * num)
    square(num)

square(5)


