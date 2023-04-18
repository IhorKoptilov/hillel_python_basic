first = 'Python'

print(first[::-1])

len_first = len(first)

list_first = list(first)

three_first = '|'.join(list_first[::3])
print(list_first)
print(three_first)


def string_to_dictionary(text=str):
    list1 = list(text)
    count = text.count(text)
    dict1 = dict.fromkeys(list1, count)
    print(dict1)
    return


def string_to_dictionary1(text1=str):
    list2 = list(text1)
    count1 = list2.__len__()
    dict2 = dict.fromkeys(text1, count1)
    print(dict2)
    return


def max_string():
    
