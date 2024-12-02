import copy

from Utilities.read_file_to_string_array import read_to_string_array


class Day2:
    arr = []

    def __init__(self, file):
        self.arr = read_to_string_array(file)

    def task1(self):
        summa = 0
        for one_line in self.arr:
            local_list = self.convert_string_array_to_int_array(one_line)

            if self.check_safety(local_list):
                summa = summa + 1

        return str(summa)

    def task2(self):
        summa = 0
        for one_line in self.arr:
            local_list = self.convert_string_array_to_int_array(one_line)

            if self.check_safety(local_list):
                summa = summa + 1
            elif self.check_safety_w_correction(local_list):
                summa = summa + 1

        return str(summa)

    def convert_string_array_to_int_array(self, loc_line):
        return [int(item) for item in loc_line.split(" ")]

    def check_safety(self, loc_arr):
        if self.check_distance(loc_arr) and (
                            self.check_monotonity(loc_arr, True)
                            or self.check_monotonity(loc_arr, False)):
            return True
        else:
            return False

    def check_safety_w_correction(self, loc_arr):
        for i in range(len(loc_arr)):
            tmp_list = copy.deepcopy(loc_arr)
            tmp_list.remove(loc_arr[i])

            if self.check_safety(tmp_list):
                return True
        return False

    def check_distance(self, loc_arr):
        i = 1
        while i < len(loc_arr):
            dist = abs(loc_arr[i - 1] - loc_arr[i])
            if dist < 1 or dist > 3:
                return False
            i = i + 1
        return True

    def check_monotonity(self, loc_arr, is_increase):
        i = 1
        while i < len(loc_arr):
            if is_increase:
                if loc_arr[i - 1] <= loc_arr[i]:
                    return False
            elif loc_arr[i - 1] >= loc_arr[i]:
                return False
            i = i + 1
        return True
