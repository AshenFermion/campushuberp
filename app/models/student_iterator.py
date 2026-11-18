class StudentIterator:
    def __init__(self, students):
        self._iterator = iter(students)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._iterator)