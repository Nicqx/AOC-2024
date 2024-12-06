from lxml.objectify import xsiannotate

from Utilities.read_file_to_string_array import read_to_string_array


class Day6:
    arr = []
    actual_poz = (0, 0,"u")
    direction = "u"
    visited = set()
    is_out = False

    def __init__(self, file):
        self.arr = read_to_string_array(file)

    def task1(self):
        self.visited.clear()
        self.is_out = False
        self.find_start()
        self.visited.add((self.actual_poz, "u"))
        while not self.is_out:
            if self.check_next():
                self.move_next()
            else:
                self.turn_left()

        return str(len(self.visited))

    def task2(self):
        summa = 0

        return str(summa)

    def find_start(self):
        for y in range(len(self.arr)):
            for x in range(len(self.arr[y])):
                if self.arr[y][x] == "^":
                    self.actual_poz = (x, y)
                    return

    def turn_left(self):
        match self.direction:
            case "u":
                self.direction = "r"
            case "l":
                self.direction = "u"
            case "d":
                self.direction = "l"
            case "r":
                self.direction = "d"

    def move_next(self):
        match self.direction:
            case "u":
                self.actual_poz = (self.actual_poz[0], self.actual_poz[1] - 1)
                self.visited.add((self.actual_poz, self.direction))
            case "l":
                self.actual_poz = (self.actual_poz[0] - 1, self.actual_poz[1])
                self.visited.add((self.actual_poz, self.direction))
            case "d":
                self.actual_poz = (self.actual_poz[0],self.actual_poz[1] + 1)
                self.visited.add((self.actual_poz, self.direction))
            case "r":
                self.actual_poz = (self.actual_poz[0] + 1, self.actual_poz[1])
                self.visited.add((self.actual_poz, self.direction))

    def check_next(self):
        match self.direction:
            case "u":
                if self.actual_poz[1] == 0:
                    self.is_out = True
                    return False
                elif self.arr[self.actual_poz[1] - 1][self.actual_poz[0]] == "#":
                    return False
                else:
                    return True
            case "l":
                if self.actual_poz[0] == 0:
                    self.is_out = True
                    return False
                elif self.arr[self.actual_poz[1]][self.actual_poz[0] - 1] == "#":
                    return False
                else:
                    return True
            case "d":
                if self.actual_poz[1] == len(self.arr) - 1:
                    self.is_out = True
                    return False
                elif self.arr[self.actual_poz[1] + 1][self.actual_poz[0]] == "#":
                    return False
                else:
                    return True
            case "r":
                if self.actual_poz[0] == len(self.arr[0]) - 1:
                    self.is_out = True
                    return False
                elif self.arr[self.actual_poz[1]][self.actual_poz[0] + 1] == "#":
                    return False
                else:
                    return True

    def correct_set(self):
        # filter out the same positions with different directions
        pass
