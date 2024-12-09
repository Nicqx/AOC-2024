from copy import deepcopy

from lxml.objectify import xsiannotate

from Utilities.read_file_to_string_array import read_to_string_array


class Day6:
    arr = []
    actual_poz = (0, 0)
    direction = "u"
    visited = set()
    is_out = False
    loop_detected = False
    loop_counter = 0

    def __init__(self, file):
        self.arr = read_to_string_array(file)

    def task1(self):
        self.visited.clear()
        self.is_out = False
        self.actual_poz = self.find_start()
        self.direction = "u"
        self.visited.add((self.actual_poz, "u"))
        while not self.is_out:
            if self.check_next(self.arr):
                self.move_next(False)
            else:
                self.turn_left()

        self.correct_set()
        return str(len(self.visited))

    def task2(self):
        self.is_out = False
        self.loop_counter = 0
        for y in range(len(self.arr)):
            for x in range(len(self.arr[y])):
                if (x == self.find_start()[0] and y == self.find_start()[1]) or self.arr[y][x] == "#":
                    break
                self.actual_poz = self.find_start()
                self.direction = "u"
                self.is_out = False
                self.loop_detected = False
                self.visited.clear()
                self.visited.add((self.actual_poz, "u"))
                local_arr = deepcopy(self.arr)
                local_arr[y] = local_arr[y][:x]+"#"+local_arr[y][x+1:]
                while not self.is_out and not self.loop_detected:
                    if self.check_next(local_arr):
                        self.move_next(True)
                    else:
                        self.turn_left()
                if self.loop_detected:
                    print("o " + str(x) + " " + str(y))
                    self.loop_counter += 1
                    self.loop_detected = False

        return str(self.loop_counter)

    def find_start(self):
        for y in range(len(self.arr)):
            for x in range(len(self.arr[y])):
                if self.arr[y][x] == "^":
                    return (x, y)

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

    def move_next(self, detect_loop):
        match self.direction:
            case "u":
                self.actual_poz = (self.actual_poz[0], self.actual_poz[1] - 1)
                if detect_loop and (self.actual_poz, self.direction) in self.visited:
                    self.loop_detected = True
                    return
                self.visited.add((self.actual_poz, self.direction))
            case "l":
                self.actual_poz = (self.actual_poz[0] - 1, self.actual_poz[1])
                if detect_loop and (self.actual_poz, self.direction) in self.visited:
                    self.loop_detected = True
                    return
                self.visited.add((self.actual_poz, self.direction))
            case "d":
                self.actual_poz = (self.actual_poz[0], self.actual_poz[1] + 1)
                if detect_loop and (self.actual_poz, self.direction) in self.visited:
                    self.loop_detected = True
                    return
                self.visited.add((self.actual_poz, self.direction))
            case "r":
                self.actual_poz = (self.actual_poz[0] + 1, self.actual_poz[1])
                if detect_loop and (self.actual_poz, self.direction) in self.visited:
                    self.loop_detected = True
                    return
                self.visited.add((self.actual_poz, self.direction))

    def check_next(self, loc_arr):
        match self.direction:
            case "u":
                if self.actual_poz[1] == 0:
                    self.is_out = True
                    return False
                elif loc_arr[self.actual_poz[1] - 1][self.actual_poz[0]] == "#":
                    return False
                else:
                    return True
            case "l":
                if self.actual_poz[0] == 0:
                    self.is_out = True
                    return False
                elif loc_arr[self.actual_poz[1]][self.actual_poz[0] - 1] == "#":
                    return False
                else:
                    return True
            case "d":
                if self.actual_poz[1] == len(loc_arr) - 1:
                    self.is_out = True
                    return False
                elif loc_arr[self.actual_poz[1] + 1][self.actual_poz[0]] == "#":
                    return False
                else:
                    return True
            case "r":
                if self.actual_poz[0] == len(loc_arr[0]) - 1:
                    self.is_out = True
                    return False
                elif loc_arr[self.actual_poz[1]][self.actual_poz[0] + 1] == "#":
                    return False
                else:
                    return True

    def correct_set(self):
        tmp = set()
        for i in self.visited:
            tmp.add(i[0])

        self.visited = tmp
