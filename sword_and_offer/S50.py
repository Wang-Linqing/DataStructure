import unittest


class Solution:
    def find_first_once_char(self, string):
        if string is None:
            return 0
        if len(string) == 0:
            return 0
        counts = {}
        for i in range(len(string)):
            if string[i] in counts.keys():
                counts[string[i]] += 1
            else:
                counts[string[i]] = 1
        for key,value in counts.items():
            if value==1:
                return key
        return 0


class Test(unittest.TestCase):
    obj = Solution()

    def test_1(self):
        self.assertEqual(self.obj.find_first_once_char("abcdefbfbfabc"), "d")

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
