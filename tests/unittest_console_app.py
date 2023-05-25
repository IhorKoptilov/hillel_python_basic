import unittest
import json
import os
from console_app import FileStorage, Pagination, App


class FileStorageTestCase(unittest.TestCase):
    def setUp(self):
        self.file_path = "test.json"
        self.storage = FileStorage.load_from_file(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_data_structure(self):
        expected_data = {}
        self.assertEqual(self.storage.data, expected_data)

        self.storage.data["courses"] = [{"name": "Python", "students": []}]
        self.storage.write_to_file()
        with open(self.file_path, "r") as file:
            data = json.load(file)
        self.assertEqual(data, self.storage.data)

    def test_get_courses(self):
        expected_courses = [{"name": "Python", "students": []}]
        self.storage.data["courses"] = expected_courses
        self.storage.write_to_file()

        loaded_storage = FileStorage.load_from_file(self.file_path)
        courses = loaded_storage.data.get("courses", [])
        self.assertEqual(courses, expected_courses)


class PaginationTestCase(unittest.TestCase):
    def test_pagination(self):
        data = [1, 2, 3, 4]
        pagination = Pagination(data, items_per_page=3)

        expected_page_data = [1, 2, 3]
        self.assertEqual(list(next(pagination)), expected_page_data)

        expected_page_data = [4]
        self.assertEqual(list(next(pagination)), expected_page_data)

        self.assertRaises(StopIteration, next, pagination)

        pagination.prev_page()
        expected_page_data = [1, 2, 3]
        self.assertEqual(list(next(pagination)), expected_page_data)

        pagination.prev_page()
        expected_page_data = [1, 2, 3]
        self.assertEqual(list(next(pagination)), expected_page_data[:-1])



class AppTestCase(unittest.TestCase):
    def test_add_student(self):
        storage = FileStorage("test.json")
        app = App(storage)
        app.add_course()
        app.add_student()

        expected_students = ["John Doe"]
        self.assertEqual(app.storage.data["courses"][0]["students"], expected_students)


if __name__ == "__main__":
    unittest.main()
