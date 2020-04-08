import unittest


class Solution:
    def is_ugly_num(self, n):
        if n is None:
            return 0
        if not n >= 1:
            return 0
        data = [0 for _ in range(n)]
        index = 0
        data[index] = 1
        index = 1
        i2 = 0
        i3 = 0
        i5 = 0
        while index <= n - 1:
            data[index] = min([data[i2] * 2, data[i3] * 3, data[i5] * 5])
            while data[i2] * 2 <= data[index]:
                i2 += 1
            while data[i3] * 3 <= data[index]:
                i3 += 1
            while data[i5] * 5 <= data[index]:
                i5 += 1
            index += 1
        return data[n - 1]


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("", "")

    def test_2(self):
        self.assertEqual("", "")

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
