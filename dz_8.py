# 1
import json


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def info(self):
        return {'first_name': self.first_name, 'last_name': self.last_name}


# 2

class Storage:
    word_list = []

    def add(self, fruit):
        self.word_list.append(fruit)
        return self.word_list

    def get(self, char):
        return sorted([fruit for fruit in self.word_list if fruit.startswith(char)])[:5]


# 3


class Course:
    students = []

    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, person):
        self.students.append(person)

    def to_json(self):
        students_info = [person.info() for person in self.students]
        # return json.dumps({'name': self.name, 'students': students_info}, sort_keys=True, indent=4)
        return {'name': self.name, 'students': students_info}


if __name__ == '__main__':
    student = Student('John', 'Doe')
    assert student.info() == {'first_name': 'John', 'last_name': 'Doe'}

    fruits_storage = Storage()
    assert fruits_storage.get('') == []
    assert fruits_storage.get('apple') == []

    fruits_storage.add('plum')
    fruits_storage.add('apple')
    fruits_storage.add('peach')
    fruits_storage.add('apricot')
    fruits_storage.add('pineapple')

    assert fruits_storage.get('') == ['apple', 'apricot', 'peach', 'pineapple', 'plum']
    assert fruits_storage.get('a') == ['apple', 'apricot']
    assert fruits_storage.get('p') == ['peach', 'pineapple', 'plum']
    assert fruits_storage.get('abc') == []

    fruits_storage.add('pear')

    assert fruits_storage.get('') == ['apple', 'apricot', 'peach', 'pear', 'pineapple']
    #
    python_basic = Course('Python basic')
    python_basic.add_student(Student('Jane', 'Doe'))
    assert python_basic.to_json() == {
        'name': 'Python basic',
        'students': [{'first_name': 'Jane', 'last_name': 'Doe'}],
    }

    python_basic.add_student(Student('John', 'Doe'))
    assert python_basic.to_json() == {
        'name': 'Python basic',
        'students': [
            {'first_name': 'Jane', 'last_name': 'Doe'},
            {'first_name': 'John', 'last_name': 'Doe'},
        ],
    }
