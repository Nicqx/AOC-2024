from unittest import TestCase

from Days.Day6 import Day6


class TestDay6(TestCase):
    def test_task1(self):
        expected_value = str(41)
        actual_value = Day6('../Resources/Day6/test1').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str(6)
        actual_value = Day6('../Resources/Day6/test1').task2()
        self.assertEqual(expected_value, actual_value)

    def test_task2_2(self):
        expected_value = str(3)
        actual_value = Day6('../Resources/Day6/test2').task2()
        self.assertEqual(expected_value, actual_value)

    def test_task2_3(self):
        expected_value = str(0)
        actual_value = Day6('../Resources/Day6/test3').task2()
        self.assertEqual(expected_value, actual_value)

    # def test_orig(self):
    #     expected_value = str(4647)
    #     actual_value = Day6('../Resources/Day6/input').task1()
    #     self.assertEqual(expected_value, actual_value)

    #     expected_value = str(22545250)
    #     actual_value = Day6('../Resources/Day6/input').task2()
    #     self.assertEqual(expected_value, actual_value)
