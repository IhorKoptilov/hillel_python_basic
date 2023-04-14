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


# d
def number1(num1):
    def number2(num2):
        return num1 * num2

    return number2


assert number1(3)(5) == 15


# e


def square(*num):
    if num > 0:
        print('*' * num)
        square(num - 1)
    return


square(5)
