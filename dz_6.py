import random
import string
import time


# a


def summ_of_items_in_list(numbers):
    summ = 0
    for item in numbers:
        if isinstance(item, list):
            summ += summ_of_items_in_list(item)
        else:
            summ += item
    return summ


assert summ_of_items_in_list([1, 2, [3, 4, [5, 6]], 7, 8, [9]]) == 45
assert summ_of_items_in_list([]) == 0
assert summ_of_items_in_list([1, 2]) == 3
assert summ_of_items_in_list([1, [2, 3, [4], [5, 6, [7]]]]) == 28


# b


def list_of_required_len(list_of_str, number):
    while len(list_of_str) != number:
        for letter in list_of_str:
            if len(list_of_str) < number:
                list_of_str.append(letter)
            elif len(list_of_str) > number:
                list_of_str.pop()
    return list_of_str


assert list_of_required_len(['a', 'b', 'c'], 7) == ['a', 'b', 'c', 'a', 'b', 'c', 'a']
assert list_of_required_len(['a', 'b', 'c'], 1) == ['a']
assert list_of_required_len(['a', 'b', 'c'], 0) == []


# c


PASSWORD = ''.join(random.choices(string.ascii_letters, k=4))


def password_checker(password):
    for real_pass_char, passed_pass_char in zip(PASSWORD, password):
        if real_pass_char != passed_pass_char:
            return

        time.sleep(0.1)


# def password_cracker():
#     password = ''.join(random.choices(string.ascii_letters, k=4))
#     start = time.time()
#     print(password)
#     password_checker(password)
#     end = time.time()
#
#     if end-start < 0.4:
#         password_cracker()
#     return print('Password correct')


def password_cracker():
    password = ''
    max_time_difference = 0.1
    while len(password) < len(PASSWORD):
        for i in string.ascii_letters:
            start = time.time()
            password_checker(password + i)
            end = time.time()
            time_difference = end - start
            if time_difference > max_time_difference:
                password += i
                max_time_difference += 0.1
        continue
    return password


password_cracker()


assert password_cracker() == PASSWORD
