import unittest


class Solution:
    def sum_is_s(self, data, s):
        if data is None:
            return None, None
        if len(data) < 2:
            return None, None
        start=0
        end=len(data)-1
        while start<=end:
            if data[start]+data[end]==s:
                return data[start],data[end]
            elif data[start]+data[end]<s:
                start+=1
            elif data[start]+data[end]>s:
                end-=1
        return None



class Test(unittest.TestCase):
    obj=Solution()
    def test_1(self):
        self.assertEqual(self.obj.sum_is_s([1,2,30,40,50,70,80,100],100),(30,70))

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
