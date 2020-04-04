import unittest


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if array is None:
            return None
        if len(array)==0:
            return None
        data=list(array)
        max_sum=[]
        for i in range(0,len(data)):
            max_sum.append(0)
        for i in range(0,len(data)):
            if i==0:
                max_sum[0]=data[i]
            else:
                if max_sum[i-1]<=0:
                    max_sum[i]=data[i]
                else:
                    max_sum[i]=max_sum[i-1]+data[i]
        return max(max_sum)

class Test(unittest.TestCase):
    obj=Solution()
    def test_1(self):
        self.assertEqual(self.obj.FindGreatestSumOfSubArray([9,-1,-1,-1,2,3,-3]),11)

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
