import unittest


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n is None:
            return 0
        data=str(n)
        return self.NumberOf1(data)
    def NumberOf1(self,strN):
        if self is None:
            return 0
        if len(strN)==0:
            return 0
        if len(strN)==1:
            if strN=="0":
                return 0
            else:
                return 1
        first_num=int(strN[0],10)
        num_of_first_num_is_one=0
        if first_num >1:
            num_of_first_num_is_one=pow(10,len(strN)-1)
        elif first_num==1:
            num_of_first_num_is_one=int(strN[1:])+1
        other_digital_is_one=first_num*(len(strN)-1)*pow(10,len(strN)-2)

        return num_of_first_num_is_one+other_digital_is_one+self.NumberOf1(strN[1:])




class Test(unittest.TestCase):
    obj=Solution()
    def test_1(self):
        self.assertEqual(self.obj.NumberOf1Between1AndN_Solution(0), 0)

    def test_2(self):
        self.assertEqual(self.obj.NumberOf1Between1AndN_Solution(10), 2)

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
