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
            raise ValueError('No previous page')

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
                '4 : Delete course''\n',
                '5 : Delete student from the course''\n',
                '6 : Exit',
            )
            item = input('Choose menu item: ')
            if item == '1':
                self.add_course()
            elif item == '2':
                self.show_courses()
            elif item == '3':
                self.add_student()
            elif item == '4':
                self.delete_course()
            elif item == '5':
                self.delete_student()
            elif item == '6':
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
            while True:
                start_index = pagination.current_page * pagination.items_per_page
                courses_on_page = next(pagination, [])
                for index, course in enumerate(courses_on_page, start=start_index):
                    course_number = index + 1
                    students = course['students']
                    if students:
                        student_names = [f"{student['first name']} {student['last name']}" for student in students]
                        students_str = ", ".join(student_names)
                        print(f'{course_number} - {course["name"]}: {students_str}')
                    else:
                        print(f'{course_number} - {course["name"]}: No students')
                command = input("Choose a course or see next/prev page: ").strip()
                if command == 'next':
                    try:
                        pagination.next_page()
                    except ValueError as e:
                        print(e)
                elif command == 'prev':
                    try:
                        pagination.prev_page()
                    except ValueError as e:
                        print(e)
                elif command.isdigit() and 1 <= int(command) <= len(courses_on_page) + start_index:
                    selected_course = courses[int(command) - 1]
                    students = selected_course['students']
                    first_name = input('Enter student\'s first name: ').strip()
                    last_name = input('Enter student\'s last name: ').strip()
                    new_student = {'first name': first_name, 'last name': last_name}
                    students.append(new_student)
                    self.storage.write_to_file()
                    print('Student added successfully!')
                    break
                else:
                    print('Invalid command')

    def delete_course(self):
        courses = self.storage.data.get('courses', [])
        if not courses:
            print('No added courses')
        else:
            print('Select a course to delete:')
            pagination = Pagination(courses)
            while True:
                start_index = pagination.current_page * pagination.items_per_page
                courses_on_page = next(pagination, [])
                for index, course in enumerate(courses_on_page, start=start_index):
                    course_number = index + 1
                    students = course['students']
                    if students:
                        student_names = [f"{student['first name']} {student['last name']}" for student in students]
                        students_str = ", ".join(student_names)
                        print(f'{course_number}: {course["name"]}, Students: {students_str}')
                    else:
                        print(f'{course_number}: {course["name"]}, No students')
                command = input("Choose a course or see next/prev page: ").strip()
                if command == 'next':
                    try:
                        pagination.next_page()
                    except ValueError as e:
                        print(e)
                elif command == 'prev':
                    try:
                        pagination.prev_page()
                    except ValueError as e:
                        print(e)
                elif command.isdigit() and 1 <= int(command) <= len(courses_on_page) + start_index:
                    course_index = int(command) - 1
                    selected_course = courses[course_index]
                    del courses[course_index]
                    print(f'Course "{selected_course["name"]}" deleted successfully')
                    self.storage.write_to_file()
                    break
                else:
                    print('Invalid input. Please try again')

    def delete_student(self):
        courses = self.storage.data.get('courses', [])
        if not courses:
            print('No added courses')
        else:
            print('Select a course to delete a student from:')
            pagination = Pagination(courses)
            while True:
                start_index = pagination.current_page * pagination.items_per_page
                courses_on_page = next(pagination, [])
                for index, course in enumerate(courses_on_page, start=start_index):
                    course_number = index + 1
                    students = course['students']
                    if students:
                        student_names = [f"{student['first name']} {student['last name']}" for student in students]
                        students_str = ", ".join(student_names)
                        print(f'{course_number}: {course["name"]}, Students: {students_str}')
                    else:
                        print(f'{course_number}: {course["name"]}, No students')
                command = input("Choose a course or see next/prev page: ").strip()
                if command == 'next':
                    try:
                        pagination.next_page()
                    except ValueError as e:
                        print(e)
                elif command == 'prev':
                    try:
                        pagination.prev_page()
                    except ValueError as e:
                        print(e)
                elif command.isdigit() and 1 <= int(command) <= len(courses_on_page) + start_index:
                    course_index = int(command) - 1
                    selected_course = courses[course_index]
                    students = selected_course['students']
                    if not students:
                        print('No students in this course')
                        break
                    print('Select a student to delete:')
                    while True:
                        for index, student in enumerate(students, start=1):
                            student_number = index
                            print(f'{student_number}: {student["first name"]} {student["last name"]}')
                        try:
                            option = input('Enter student number (0 to cancel): ')
                            if option == '0':
                                break
                            option = int(option)
                            student_index = option - 1
                            del students[student_index]
                            print('Student deleted successfully')
                            self.storage.write_to_file()
                            break
                        except ValueError:
                            print('Invalid input. Please try again')
                        except IndexError:
                            print('Invalid student number. Please try again')
                        except Exception as e:
                            print(f'An error occurred: {str(e)}')
                    break
                else:
                    print('Invalid input. Please try again')

    def show_courses(self):
        courses = self.storage.data.get('courses', [])
        if not courses:
            print('No added courses')
        else:
            print('Courses:')
            for index, course in enumerate(courses, start=1):
                students = course['students']
                if students:
                    students_str = ', '.join(
                        [f"{i + 1}. {student['first name']} {student['last name']}" for i, student in
                         enumerate(students)])
                    print(f'{index} - {course["name"]} (Students: {students_str})')
                else:
                    print(f'{index} - {course["name"]} (No students in this course)')

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
