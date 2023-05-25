import os
import json
import pytest
from console_app import FileStorage, Pagination, App


@pytest.fixture
def file_path(tmp_path):
    path = tmp_path / "test_storage.json"
    return str(path)


def test_file_storage(file_path):
    storage = FileStorage(file_path)

    assert storage.data == {}

    storage.data = {"courses": [{"name": "Math", "students": []}]}
    storage.write_to_file()
    assert os.path.exists(file_path)

    loaded_storage = FileStorage.load_from_file(file_path)
    assert loaded_storage.data == storage.data

    storage.data.setdefault('courses', []).append({'name': 'English', 'students': []})
    storage.write_to_file()
    loaded_storage = FileStorage.load_from_file(file_path)
    assert len(loaded_storage.data['courses']) == 2
    assert loaded_storage.data['courses'][1]['name'] == 'English'


def test_pagination():
    data = [1, 2, 3, 4]
    pagination = Pagination(data, items_per_page=3)

    assert next(pagination) == [1, 2, 3]

    assert next(pagination) == [4]

    with pytest.raises(StopIteration):
        next(pagination)

    pagination.prev_page()
    assert next(pagination) == [1, 2, 3]

    pagination.prev_page()
    assert next(pagination) == [1, 2, 3]


def test_app():
    course = App("Math")

    course.add_student("John Doe")
    assert course.get_students() == ["John Doe"]

    course.add_student("Jane Smith")
    course.add_student("Alice Johnson")
    assert course.get_students() == ["John Doe", "Jane Smith", "Alice Johnson"]
