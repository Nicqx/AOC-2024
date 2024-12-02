import copy

from Utilities.read_file_to_string_array import read_to_string_array


def convert_string_array_to_int_array(loc_line):
    return [int(item) for item in loc_line.split(" ")]


def check_distance(loc_arr):
    i = 1
    while i < len(loc_arr):
        dist = abs(loc_arr[i - 1] - loc_arr[i])
        if dist < 1 or dist > 3:
            return False
        i = i + 1
    return True


def check_if_monotone(loc_arr, is_increase):
    i = 1
    while i < len(loc_arr):
        if is_increase:
            if loc_arr[i - 1] >= loc_arr[i]:
                return False
        elif loc_arr[i - 1] <= loc_arr[i]:
            return False
        i = i + 1
    return True


def check_safety(loc_arr):
    if check_distance(loc_arr) and (
            check_if_monotone(loc_arr, True)
            or check_if_monotone(loc_arr, False)):
        return True
    else:
        return False


def check_safety_w_correction(loc_arr):
    for i in range(len(loc_arr)):
        tmp_list = copy.deepcopy(loc_arr)
        # tmp_list.remove(loc_arr[i]) not ok, because if duplicate elements are exist and the second should be removed
        del tmp_list[i]

        if check_safety(tmp_list):
            return True
    return False


class Day2:
    arr = []

    def __init__(self, file):
        self.arr = read_to_string_array(file)

    def task1(self):
        summa = 0
        for one_line in self.arr:
            local_list = convert_string_array_to_int_array(one_line)

            if check_safety(local_list):
                summa = summa + 1

        return str(summa)

    def task2(self):
        summa = 0
        for one_line in self.arr:
            local_list = convert_string_array_to_int_array(one_line)

            if check_safety(local_list):
                summa = summa + 1
            elif check_safety_w_correction(local_list):
                summa = summa + 1

        return str(summa)
