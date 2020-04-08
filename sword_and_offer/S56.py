import unittest


class Solution:
    def find_two_number(self, data):
        if data is None:
            return None, None
        if len(data) <= 2:
            return None, None
        result = 0
        for i in range(0, len(data)):
            result ^= data[i]
        one = 1
        count = 0
        for i in range(0, 32):
            ret=result & one
            if ret >0:
                break
            else:
                one = one << 1
                count += 1
        if count == 32:
            return None, None
        num_1=0
        num_2=0
        for i in range(len(data)):
            if one&data[i]==0:
                num_1^=data[i]
            else:
                num_2^=data[i]
        return num_1,num_2

class Test(unittest.TestCase):
    obj=Solution()
    def test_1(self):
        self.assertEqual(self.obj.find_two_number([2,4,3,6,3,2,5,5]), (4,6))

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
