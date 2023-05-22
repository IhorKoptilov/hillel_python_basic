import json
import os
import sys


class Pagination:
    def __init__(self, data, items_per_page=3):
        self.data = data
        self.items_per_page = items_per_page
        self.current_page = 0

    def __iter__(self):
        return self

    def __next__(self):
        start = self.current_page * self.items_per_page
        end = start + self.items_per_page
        items = self.data[start:end]
        return items

    def next_page(self):
        if self.current_page < self.get_total_pages() - 1:
            self.current_page += 1
        else:
            raise ValueError('No next page')

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
        else:
            print('No previous page')

    # def get_current_page_data(self):
    #     start = (self.page_number - 1) * self.page_size
    #     end = self.page_number * self.page_size
    #     self.current_page_data = self.data[start:end]
    #     return self.current_page_data

    def get_total_pages(self):
        return len(self.data) // self.items_per_page + (len(self.data) % self.items_per_page > 0)


class FileStorage:
    data = None
    file_path = None

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}

    @staticmethod
    def load_from_file(file_path):
        storage = FileStorage(file_path)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                storage.data = json.load(file)
        return storage

    def write_to_file(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file)


class App:
    def __init__(self, storage):
        self.storage = storage

    def run(self):
        while True:
            print(
                ' 1 : Add course''\n',
                '2 : Show courses''\n',
                '3 : Add student to the course''\n',
                '4 : Exit',
            )
            item = input('Choose menu item: ')
            if item == '1':
                self.add_course()
            elif item == '2':
                self.show_courses()
            elif item == '3':
                self.add_student()
            elif item == '4':
                self.exit()
            else:
                print('No such menu item. Please, try again')

    def add_course(self):
        print('Adding course')
        name = input('Enter course name: ')
        self.storage.data.setdefault('courses', []).append({'name': name, 'students': []})
        print('Course added successfully')
        self.storage.write_to_file()

    def add_student(self):
        courses = self.storage.data.get('courses', [])
        if not courses:
            print('No added courses')
        else:
            print('Select a course to add a student:')
            pagination = Pagination(courses)
            self.pagination = iter(pagination)
            current_page = 0
            while True:
                start_index = current_page * pagination.items_per_page
                for index, course in enumerate(next(self.pagination), start=start_index):
                    course_number = index + 1
                    print(f'{course_number} - {course["name"]}')
                command = input("Choose a course or see next/prev page: ")
                if command == 'next':
                    try:
                        self.pagination.next_page()
                        current_page += 1
                    except ValueError as e:
                        print(e)
                elif command == 'prev':
                    try:
                        self.pagination.prev_page()
                        current_page -= 1
                    except ValueError as e:
                        print(e)
                elif command.isdigit() and 1 <= int(command) <= len(self.pagination.data):
                    selected_course = self.pagination.data[int(command) - 1]
                    first_name = input("Enter student's first name: ")
                    last_name = input("Enter student's last name: ")
                    selected_course['students'].append({'first name': first_name, 'last name': last_name})
                    self.storage.write_to_file()
                    print("Student added successfully!")
                    break
                else:
                    print('Invalid command')

    def show_courses(self):
        courses = self.storage.data.get('courses', [])
        if not courses:
            print('No added courses')
        else:
            print('Courses:')
            for index, course in enumerate(courses, start=1):
                print(f'{index} - {course["name"]}')

    # def select_courses(self):
    #     courses = self.storage.data.get('courses', [])
    #     number = 1
    #     print('Chose a course to add student in: ')
    #     for course in courses:
    #         print(number, '-',  course['name'])
    #         number += 1
    #     print('Chose a course or see/prev page: ')

    def exit(self):
        self.storage.write_to_file()
        sys.exit()


if __name__ == '__main__':
    file_path = input('Enter storage path: ')
    app = App(FileStorage.load_from_file(file_path))
    app.run()
