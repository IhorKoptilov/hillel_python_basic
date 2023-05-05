import json


class JsonParser:
    data = None

    def __init__(self, json_data):
        self.json_data = json_data

    def json_to_python_data(self):
        return json.loads(self.json_data)

    def __enter__(self):
        self.data = self.json_to_python_data()
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def contains(self, point):
        x, y = point.x, point.y
        if self.left.x <= x <= self.right.x and self.left.y <= y <= self.right.y:
            return True
        return False

    def __contains__(self, point):
        return self.contains(point)


if __name__ == '__main__':

    with JsonParser('"hello"') as res:
        assert res == "hello"

    with JsonParser('{"hello": "world", "key": [1,2,3]}') as res:
        assert res == {"hello": "world", "key": [1, 2, 3]}

    start_point = Point(1, 0)
    end_point = Point(7, 3)

    rect = Rectangle(start_point, end_point)
    assert rect.contains(start_point)
    assert not rect.contains(Point(-1, 3))
    assert start_point in rect
    assert Point(-1, 3) not in rect
