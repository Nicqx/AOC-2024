from Utilities.read_file_to_string_array import read_to_string_array


class Day5:
    arr = []
    rules = []
    updates = []
    update2 = []

    def __init__(self, file):
        self.arr.clear()
        self.rules.clear()
        self.updates.clear()
        self.update2.clear()
        self.arr = read_to_string_array(file)
        self.process_rules_and_upds()

    def task1(self):
        summa = 0
        for i in range(len(self.updates)):
            if self.validate_upd(i):
                summa = summa + self.updates[i][int(len(self.updates[i]) / 2)]

        return str(summa)

    def task2(self):
        summa = 0
        for i in range(len(self.updates)):
            if not (self.validate_upd(i)):
                self.update2.append(self.updates[i])

        for i in range(len(self.update2)):
            while not (self.validate_upd_w_correction(i)):
                pass

        for i in range(len(self.update2)):
            summa = summa + self.update2[i][int(len(self.update2[i]) / 2)]

        return str(summa)

    def validate_upd(self, index_of_rules):
        for item in range(len(self.rules)):
            low = int(self.rules[item][0])
            high = int(self.rules[item][1])
            try:
                index_of_low_in_upds = self.updates[index_of_rules].index(low)
                index_of_high_in_upds = self.updates[index_of_rules].index(high)
                if index_of_low_in_upds > index_of_high_in_upds:
                    return False
            except ValueError:
                pass
        return True

    def validate_upd_w_correction(self, index_of_rules):
        for item in range(len(self.rules)):
            low = int(self.rules[item][0])
            high = int(self.rules[item][1])
            try:
                index_of_low_in_upds = self.update2[index_of_rules].index(low)
                index_of_high_in_upds = self.update2[index_of_rules].index(high)
                if index_of_low_in_upds > index_of_high_in_upds:
                    self.update2[index_of_rules][index_of_low_in_upds], self.update2[index_of_rules][
                        index_of_high_in_upds] = self.update2[index_of_rules][index_of_high_in_upds], \
                    self.update2[index_of_rules][index_of_low_in_upds]
                    return False
            except ValueError:
                pass
        return True

    def process_rules_and_upds(self):
        i = 0
        while self.arr[i] != "":
            tmp = []
            for e in self.arr[i].split("|"):
                tmp.append(int(e))
            self.rules.append(tmp)
            i = i + 1
        i = i + 1
        while i < len(self.arr):
            tmp = []
            for e in self.arr[i].split(","):
                tmp.append(int(e))
            self.updates.append(tmp)
            i = i + 1
