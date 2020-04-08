import unittest


class Solution:
    def reverse_string(self,string:str):
        if string is None:
            return None
        if len(string)==0:
            return string
        data_list=string.split(" ")
        data_list.reverse()
        tmp=""
        for item in data_list:
            tmp=tmp+" "+item
        return tmp[1:]


class Test(unittest.TestCase):
    obj=Solution()
    def test_1(self):
        self.assertEqual(self.obj.reverse_string("I am a student."), "student. a am I")

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
