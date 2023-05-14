import json
import os
import sys


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

    menu_items = None

    def __init__(self, storage):
        self.storage = storage

    def run(self):
        while True:
            print(
                ' 1 : Add course''\n',
                '2 : Show courses''\n',
                '3 : Exit',
            )
            item = input('Choose menu item: ')
            if item == '1':
                self.add_course()
            elif item == '2':
                self.show_courses()
            elif item == '3':
                self.exit()
            else:
                print('No such menu item. Please, try again')

    def add_course(self):
        print('Adding course')
        name = input('Enter course name: ')
        self.storage.data.setdefault('courses', []).append({'name': name})
        self.storage.write_to_file()

    def show_courses(self):
        courses = self.storage.data.get('courses', [])
        if not courses:
            print('No added courses')
        else:
            print('Courses list')
            for course in courses:
                print(course['name'])

    def exit(self):
        self.storage.write_to_file()
        sys.exit()


if __name__ == '__main__':
    file_path = input('Enter storage path: ')
    app = App(FileStorage.load_from_file(file_path))
    app.run()
