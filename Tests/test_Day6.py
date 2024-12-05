from unittest import TestCase

from Days.Day6 import Day6


class TestDay1(TestCase):
    def test_task1(self):
        expected_value = str(11)
        actual_value = Day6('../Resources/Day6/test1').task1()
        self.assertEqual(expected_value, actual_value)

    # def test_task2(self):
    #     expected_value = str(31)
    #     actual_value = Day6('../Resources/Day6/test1').task2()
    #     self.assertEqual(expected_value, actual_value)
    #
    # def test_orig(self):
    #     expected_value = str(1222801)
    #     actual_value = Day6('../Resources/Day6/input').task1()
    #     self.assertEqual(expected_value, actual_value)
    #
    #     expected_value = str(22545250)
    #     actual_value = Day6('../Resources/Day6/input').task2()
    #     self.assertEqual(expected_value, actual_value)
