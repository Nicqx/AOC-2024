from Utilities.read_file_to_string_array import read_to_string_array


class Day4:
    arr = []

    def __init__(self, file):
        self.arr = read_to_string_array(file)

    def task1(self):
        summa = 0
        for y in range(len(self.arr)):
            for x in range(len(self.arr[y])):
                if self.check_up(x, y):
                    summa = summa + 1
                if self.check_down(x, y):
                    summa = summa + 1
                if self.check_left(x, y):
                    summa = summa + 1
                if self.check_right(x, y):
                    summa = summa + 1
                if self.check_upper_right(x, y):
                    summa = summa + 1
                if self.check_lower_right(x, y):
                    summa = summa + 1
                if self.check_upper_left(x, y):
                    summa = summa + 1
                if self.check_lower_left(x, y):
                    summa = summa + 1

        return str(summa)

    def task2(self):
        summa = 0
        for y in range(len(self.arr)):
            for x in range(len(self.arr[y])):
                if (self.check_x_down(x, y) or
                        self.check_x_up(x, y) or
                        self.check_x_up_down(x, y) or
                        self.check_x_down_up(x, y)):
                    summa = summa + 1
        return str(summa)

    def check_x_down(self, x, y):
        if x < 1 or x >= len(self.arr[y]) - 1 or y < 1 or y >= len(self.arr) - 1:
            return False
        if self.arr[y][x] != "A":
            return False
        elif self.arr[y - 1][x - 1] != "M":
            return False
        elif self.arr[y + 1][x + 1] != "S":
            return False
        elif self.arr[y - 1][x + 1] != "S":
            return False
        elif self.arr[y + 1][x - 1] != "M":
            return False
        else:
            return True

    def check_x_up(self, x, y):
        if x < 1 or x >= len(self.arr[y]) - 1 or y < 1 or y >= len(self.arr) - 1:
            return False
        if self.arr[y][x] != "A":
            return False
        elif self.arr[y - 1][x - 1] != "S":
            return False
        elif self.arr[y + 1][x + 1] != "M":
            return False
        elif self.arr[y - 1][x + 1] != "S":
            return False
        elif self.arr[y + 1][x - 1] != "M":
            return False
        else:
            return True

    def check_x_up_down(self, x, y):
        if x < 1 or x >= len(self.arr[y]) - 1 or y < 1 or y >= len(self.arr) - 1:
            return False
        if self.arr[y][x] != "A":
            return False
        elif self.arr[y - 1][x - 1] != "S":
            return False
        elif self.arr[y + 1][x + 1] != "M":
            return False
        elif self.arr[y - 1][x + 1] != "M":
            return False
        elif self.arr[y + 1][x - 1] != "S":
            return False
        else:
            return True

    def check_x_down_up(self, x, y):
        if x < 1 or x >= len(self.arr[y]) - 1 or y < 1 or y >= len(self.arr) - 1:
            return False
        if self.arr[y][x] != "A":
            return False
        elif self.arr[y - 1][x - 1] != "M":
            return False
        elif self.arr[y + 1][x + 1] != "S":
            return False
        elif self.arr[y - 1][x + 1] != "M":
            return False
        elif self.arr[y + 1][x - 1] != "S":
            return False
        else:
            return True

    def check_right(self, x, y):
        if x >= len(self.arr[y]) - 3:
            return False
        if self.arr[y][x] != "X":
            return False
        elif self.arr[y][x + 1] != "M":
            return False
        elif self.arr[y][x + 2] != "A":
            return False
        elif self.arr[y][x + 3] != "S":
            return False
        else:
            return True

    def check_upper_right(self, x, y):
        if x >= len(self.arr[y]) - 3 or y < 3:
            return False
        if self.arr[y][x] != "X":
            return False
        elif self.arr[y - 1][x + 1] != "M":
            return False
        elif self.arr[y - 2][x + 2] != "A":
            return False
        elif self.arr[y - 3][x + 3] != "S":
            return False
        else:
            return True

    def check_lower_right(self, x, y):
        if x >= len(self.arr[y]) - 3 or y >= len(self.arr) - 3:
            return False
        if self.arr[y][x] != "X":
            return False
        elif self.arr[y + 1][x + 1] != "M":
            return False
        elif self.arr[y + 2][x + 2] != "A":
            return False
        elif self.arr[y + 3][x + 3] != "S":
            return False
        else:
            return True

    def check_left(self, x, y):
        if x < 3:
            return False
        if self.arr[y][x] != "X":
            return False
        elif self.arr[y][x - 1] != "M":
            return False
        elif self.arr[y][x - 2] != "A":
            return False
        elif self.arr[y][x - 3] != "S":
            return False
        else:
            return True

    def check_upper_left(self, x, y):
        if x < 3 or y < 3:
            return False
        if self.arr[y][x] != "X":
            return False
        elif self.arr[y - 1][x - 1] != "M":
            return False
        elif self.arr[y - 2][x - 2] != "A":
            return False
        elif self.arr[y - 3][x - 3] != "S":
            return False
        else:
            return True

    def check_lower_left(self, x, y):
        if x < 3 or y >= len(self.arr) - 3:
            return False
        if self.arr[y][x] != "X":
            return False
        elif self.arr[y + 1][x - 1] != "M":
            return False
        elif self.arr[y + 2][x - 2] != "A":
            return False
        elif self.arr[y + 3][x - 3] != "S":
            return False
        else:
            return True

    def check_down(self, x, y):
        if y >= len(self.arr) - 3:
            return False
        if self.arr[y][x] != "X":
            return False
        elif self.arr[y + 1][x] != "M":
            return False
        elif self.arr[y + 2][x] != "A":
            return False
        elif self.arr[y + 3][x] != "S":
            return False
        else:
            return True

    def check_up(self, x, y):
        if y < 3:
            return False
        if self.arr[y][x] != "X":
            return False
        elif self.arr[y - 1][x] != "M":
            return False
        elif self.arr[y - 2][x] != "A":
            return False
        elif self.arr[y - 3][x] != "S":
            return False
        else:
            return True
