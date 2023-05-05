import random


# 1


def retry(attempts=5, desired_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            num = 0
            while num < attempts:
                value = func(*args, **kwargs)
                if value == desired_value:
                    break
                print("Cannot reach expected value")
                num += 1
            return value
        return wrapper
    return decorator


@retry(desired_value=3)
def get_random_value_with_default_attempts():
    return random.choice((1, 2, 3, 4, 5))


@retry(desired_value=[1, 2])
def get_random_values_with_default_attempts(choices, size=2):
    return random.choices(choices, k=size)


@retry(attempts=7, desired_value=3)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry(attempts=2, desired_value=[1, 2, 3])
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


get_random_value()
get_random_value_with_default_attempts()
get_random_values_with_default_attempts([1, 2, 3, 4])
get_random_values_with_default_attempts([1, 2, 3, 4], 2)
get_random_values_with_default_attempts([1, 2, 3, 4], size=2)
get_random_values_with_default_attempts(choices=[1, 2, 3, 4], size=2)
get_random_values([1, 2, 3, 4])
get_random_values([1, 2, 3, 4], 3)
get_random_values([1, 2, 3, 4], size=1)


# 2


def file_copier(path_to_copy, path_to_paste):
    with open(path_to_copy, 'r', encoding='windows-1251') as file_to_copy:
        with open(path_to_paste, 'w', encoding='windows-1251') as file_to_paste:
            file_to_paste.write(file_to_copy.read())


# 3


def read_file(path_to_file):
    line_count = 0
    file_size = 0
    top_chars = {}
    with open(path_to_file, 'r', encoding='windows-1251') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line_count += 1
            file_size += len(line)
            for char in line:
                if char not in ('\n', ' '):
                    top_chars[char] = top_chars.get(char, 0) + 1
    top_chars = dict(sorted(top_chars.items(), key=lambda x: x[1], reverse=True)[:3])
    return print({'line_count': line_count, 'file_size': file_size, 'top_chars': top_chars})
