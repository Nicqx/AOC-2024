from unittest import TestCase

from Days.Day4 import Day4


class TestDay4(TestCase):
    def test_check_right_t(self):
        expected_value = True
        actual_value = Day4('../Resources/Day4/test2').check_right(0, 3)
        self.assertEqual(expected_value, actual_value)

    def test_check_right_f(self):
        expected_value = False
        actual_value = Day4('../Resources/Day4/test2').check_right(0, 4)
        self.assertEqual(expected_value, actual_value)

    def test_check_upper_right_t(self):
        expected_value = True
        actual_value = Day4('../Resources/Day4/test2').check_upper_right(0, 6)
        self.assertEqual(expected_value, actual_value)

    def test_check_upper_right_f(self):
        expected_value = False
        actual_value = Day4('../Resources/Day4/test2').check_upper_right(0, 4)
        self.assertEqual(expected_value, actual_value)

    def test_check_lower_right_t(self):
        expected_value = True
        actual_value = Day4('../Resources/Day4/test2').check_lower_right(0, 0)
        self.assertEqual(expected_value, actual_value)

    def test_check_lower_right_f(self):
        expected_value = False
        actual_value = Day4('../Resources/Day4/test2').check_lower_right(0, 4)
        self.assertEqual(expected_value, actual_value)

    def test_check_left_t(self):
        expected_value = True
        actual_value = Day4('../Resources/Day4/test2').check_left(6, 3)
        self.assertEqual(expected_value, actual_value)

    def test_check_left_f(self):
        expected_value = False
        actual_value = Day4('../Resources/Day4/test2').check_left(0, 4)
        self.assertEqual(expected_value, actual_value)

    def test_check_upper_left_t(self):
        expected_value = True
        actual_value = Day4('../Resources/Day4/test2').check_upper_left(6, 6)
        self.assertEqual(expected_value, actual_value)

    def test_check_upper_left_f(self):
        expected_value = False
        actual_value = Day4('../Resources/Day4/test2').check_upper_left(0, 4)
        self.assertEqual(expected_value, actual_value)

    def test_check_lower_left_t(self):
        expected_value = True
        actual_value = Day4('../Resources/Day4/test2').check_lower_left(6, 0)
        self.assertEqual(expected_value, actual_value)

    def test_check_lower_left_f(self):
        expected_value = False
        actual_value = Day4('../Resources/Day4/test2').check_lower_left(0, 4)
        self.assertEqual(expected_value, actual_value)

    def test_check_down_t(self):
        expected_value = True
        actual_value = Day4('../Resources/Day4/test2').check_down(3, 0)
        self.assertEqual(expected_value, actual_value)

    def test_check_down_f(self):
        expected_value = False
        actual_value = Day4('../Resources/Day4/test2').check_down(0, 3)
        self.assertEqual(expected_value, actual_value)

    def test_check_up_t(self):
        expected_value = True
        actual_value = Day4('../Resources/Day4/test2').check_up(3, 6)
        self.assertEqual(expected_value, actual_value)

    def test_check_up_f(self):
        expected_value = False
        actual_value = Day4('../Resources/Day4/test2').check_up(0, 3)
        self.assertEqual(expected_value, actual_value)

    def test_task1(self):
        expected_value = str(18)
        actual_value = Day4('../Resources/Day4/test1').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task1_2(self):
        expected_value = str(8)
        actual_value = Day4('../Resources/Day4/test2').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2_2(self):
        expected_value = str(1)
        actual_value = Day4('../Resources/Day4/test3').task2()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str(9)
        actual_value = Day4('../Resources/Day4/test1').task2()
        self.assertEqual(expected_value, actual_value)

    def test_orig(self):
        expected_value = str(2642)
        actual_value = Day4('../Resources/Day4/input').task1()
        self.assertEqual(expected_value, actual_value)

        expected_value = str(1974)
        actual_value = Day4('../Resources/Day4/input').task2()
        self.assertEqual(expected_value, actual_value)
