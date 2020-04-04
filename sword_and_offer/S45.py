import unittest


def is_equal(str_1, str2):
    m = str_1 + str2
    n = str2 + str_1
    _m = int(m, 10)
    _n = int(n, 10)
    if _m == _n:
        return 0
    elif _m > _n:
        return 1
    else:
        return -1


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if numbers is None:
            return 0
        if len(numbers) == 0:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        data = []
        for item in numbers:
            data.append(str(item))
        length = 0
        for item in data:
            length += len(item)
        self.sort(data, 0, len(data) - 1)
        print(data)
        result=""
        for item in data:
            result+=item
        print(result)
        return int(result,10)

    def sort(self, data, start, end):
        index = self.partition(data, start, end)
        if index > start:
            self.sort(data, start, index - 1)
        elif index < end:
            self.sort(data, index + 1, end)

    def partition(self, data, start, end):
        if data == None or start < 0 or end >= len(data) or end < start:
            raise ValueError
        index = start
        self.swap(data, index, end)
        small = start - 1
        for i in range(start, end):
            ret = is_equal(data[i], data[end])
            if ret == -1:
                small += 1
                if i != small:
                    self.swap(data, i, small)
        small += 1
        self.swap(data, small, end)
        return small

    def swap(self, data, index1, index2):
        tmp = data[index1]
        data[index1] = data[index2]
        data[index2] = tmp


class Test(unittest.TestCase):
    obj = Solution()

    def test_1(self):
        self.assertEqual(self.obj.PrintMinNumber([1,  3, 4, 12]), 11234)



    def test_2(self):
        self.assertEqual(self.obj.PrintMinNumber([3, 32, 321]), 321323)

    def test_3(self):
        self.assertEqual("", "")

    def test_4(self):
        self.assertEqual("", "")

    def test_5(self):
        self.assertEqual("", "")

    def test_6(self):
        self.assertEqual("", "")

    def test_7(self):
        self.assertEqual("", "")

    def test_8(self):
        self.assertEqual("", "")
