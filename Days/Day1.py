import re

from Utilities.read_file_to_string_array import read_to_string_array


class Day1:
    arr = []

    def __init__(self, file):
        self.arr = read_to_string_array(file)

    def task1(self):
        left = []
        right = []
        summa = 0
        for element in self.arr:
            pattern = r'(\d+)\s+(\d+)'
            match = re.search(pattern, element)
            left.append(int(match.group(1)))
            right.append(int(match.group(2)))
        left.sort()
        right.sort()

        while left:
            summa += abs(left[0] - right[0])
            left = left[1:]
            right = right[1:]

        return str(summa)

    def task2(self):
        left = []
        right = []
        summa = 0
        for element in self.arr:
            pattern = r'(\d+)\s+(\d+)'
            match = re.search(pattern, element)
            left.append(int(match.group(1)))
            right.append(int(match.group(2)))

        for element in left:
            summa += right.count(element) * element

        return str(summa)
