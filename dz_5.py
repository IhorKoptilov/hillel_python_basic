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
    

    
    
def sort_and_join_words(string, separator):
    # Розбиваємо рядок на список слів за допомогою заданого роздільника
    words = string.split(separator)
    # Сортуємо список слів
    sorted_words = sorted(words)
    # Склеюємо відсортовані слова за допомогою заданого роздільника
    sorted_string = separator.join(sorted_words)
    # Повертаємо відсортований рядок слів
    return sorted_string
    print(sorted_string)


sort_and_join_words('Hello world Alex Bill', '/')
