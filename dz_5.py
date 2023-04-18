first = 'Python'

print(first[::-1])

len_first = len(first)

list_first = list(first)

three_first = '|'.join(list_first[::3])


def string_to_dictionary(text):
    dict1 = {}
    for letter in text:
        dict1[letter] = text.count(letter)
    return print(dict1)


string_to_dictionary('buzzing')


def count_letters(text):
    letter_count = {}
    for letter in text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return print(letter_count)


print(count_letters('CHERRIES'))


def max_string(strings):
    longest_string = ""
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string


assert max_string(['pass', 'algorithm', 'write', 'a', 'program', 'test', 'program']) == 'algorithm'


def sorted_and_glue_words(string, separator):
    words = string.split(separator)
    sorted_words = sorted(words)
    sorted_string = separator.join(sorted_words)
    return sorted_string


assert sorted_and_glue_words('c+f+d+a+b', '+') == 'a+b+c+d+f'


def ascii_to_string(numbers):
    ascii_str = ""
    for num in numbers:
        ascii_char = chr(num)
        ascii_str += ascii_char
    return print(ascii_str)


ascii_to_string([119, 101, 108, 108, 32, 100, 111, 110, 101])
