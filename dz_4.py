# a

def positional_arguments(*args):
    """Function return list of an unspecified number of arguments"""
    return list(set(args))


print(positional_arguments('Bob', 'Pete', False, None, 5, 4, 5))


# b


def named_arguments(**user_data):
    print(len(user_data))
    print(user_data['user_type'])


named_arguments(user_type='Student', user_name='Bob', user_age=23, user_sex='male')


# c


def mixed_arguments(positional1, positional2, /, mixed, *, named, five=5, six=6):
    pass


mixed_arguments(1, 2, mixed=3, named=4, five=5, six=6)


# d
def number1(num1):
    def number2(num2):
        return num1 * num2

    return number2


assert number1(3)(5) == 15


# e


def square(num, num1=0):
    if num1 == num:
        return
    print('*' * num)
    square(num, num1 + 1)
    return


square(4)
