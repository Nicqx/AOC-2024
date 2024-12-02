from unittest import TestCase

from Days.Day2 import Day2


class TestDay2(TestCase):

    def test_check_distance(self):
        arr_true = [7, 6, 4, 2, 1]
        expected_value = True
        actual_value = Day2('../Resources/Day2/test1').check_distance(arr_true)
        self.assertEqual(expected_value, actual_value)

    def test_check_distance2(self):
        arr_false = [9, 7, 6, 2, 1]
        expected_value = False
        actual_value = Day2('../Resources/Day2/test1').check_distance(arr_false)
        self.assertEqual(expected_value, actual_value)

    def test_check_distance3(self):
        arr_false2 = [9, 7, 6, 6, 5]
        expected_value = False
        actual_value = Day2('../Resources/Day2/test1').check_distance(arr_false2)
        self.assertEqual(expected_value, actual_value)

    def test_check_increase(self):
        arr_true = [7, 6, 4, 2, 1]
        expected_value = True
        actual_value = Day2('../Resources/Day2/test1').check_monotonity(arr_true, True)
        self.assertEqual(expected_value, actual_value)

    def test_check_decrease(self):
        arr_true = [1, 2, 4, 6, 7]
        expected_value = True
        actual_value = Day2('../Resources/Day2/test1').check_monotonity(arr_true, False)
        self.assertEqual(expected_value, actual_value)

    def test_check_increase2(self):
        arr_true = [7, 6, 4, 5, 1]
        expected_value = False
        actual_value = Day2('../Resources/Day2/test1').check_monotonity(arr_true, True)
        self.assertEqual(expected_value, actual_value)

    def test_check_decrease2(self):
        arr_true = [1, 5, 4, 6, 7]
        expected_value = False
        actual_value = Day2('../Resources/Day2/test1').check_monotonity(arr_true, False)
        self.assertEqual(expected_value, actual_value)

    def test_task1(self):
        expected_value = str(2)
        actual_value = Day2('../Resources/Day2/test1').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str(4)
        actual_value = Day2('../Resources/Day2/test1').task2()
        self.assertEqual(expected_value, actual_value)

def test_orig(self):
    expected_value = str(220)
    actual_value = Day2('../Resources/Day2/input').task1()
    self.assertEqual(expected_value, actual_value)
#
#     expected_value = str(147)
#     actual_value = Day2('../Resources/Day2/input').task2()
#     self.assertEqual(expected_value, actual_value)
