from unittest import TestCase

from Days.Day3 import Day3


class TestDay3(TestCase):
    def test_task1(self):
        expected_value = str(161)
        actual_value = Day3('../Resources/Day3/test1').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str(48)
        actual_value = Day3('../Resources/Day3/test2').task2()
        self.assertEqual(expected_value, actual_value)

    def test_task3(self):
        expected_value = str(48)
        actual_value = Day3('../Resources/Day3/test3').task2()
        self.assertEqual(expected_value, actual_value)


    def test_orig(self):
        expected_value = str(190604937)
        actual_value = Day3('../Resources/Day3/input').task1()
        self.assertEqual(expected_value, actual_value)

        expected_value = str(82857512)
        actual_value = Day3('../Resources/Day3/input').task2()
        self.assertEqual(expected_value, actual_value)
