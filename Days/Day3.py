import re

from Utilities.read_file_to_string_array import read_to_string_array


class Day3:
    arr = []

    def __init__(self, file):
        self.arr = read_to_string_array(file)

    def task1(self):
        summa = 0
        pattern = r'(mul\((\d+),(\d+)\))'
        for line in self.arr:
            result = re.findall(pattern, line)
            for items in result:
                summa = summa + int(items[1]) * int(items[2])

        return str(summa)

    def task2(self):
        summa = 0
        new_str = ''.join(self.arr[:])

        pattern = r'don\'t\(\).*?do\(\)'
        replace = ''
        new_str = re.sub(pattern, replace, new_str)

        pattern = r'(mul\((\d+),(\d+)\))'
        result = re.findall(pattern, new_str)
        for items in result:
            summa = summa + int(items[1]) * int(items[2])

        return str(summa)
