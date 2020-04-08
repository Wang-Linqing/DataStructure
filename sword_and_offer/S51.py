import unittest


class Solution:
    def inverse_pairs(self, data):
        if data is None:
            return 0
        if len(data) == 0:
            return 0
        return self.core(data,0,len(data)-1)
    def core(self,data,start,end):
        if start>end:
            raise ValueError
        if end-start+1==1:
            return 0
        if end-start+1==2:
            if data[start]>data[end]:
                tmp=data[start]
                data[start]=data[end]
                data[end]=tmp
                return 1
            else:
                return 0
        count_1=self.core(data,start,(start+end)//2)
        count_2=self.core(data,(start+end)//2+1,end)
        count_3=0
        for i in range(start,(start+end)//2+1):
            j=(start+end)//2+1
            while j<=end:
                if data[i]>data[j]:
                    count_3+=1
                    j+=1
                else:
                    break
        tmp=data[start:end+1]
        tmp.sort()
        data[start:end + 1]=tmp
        return count_1+count_2+count_3
    def swap(self,data,i,j):
        tmp=data[i]
        data[i]=data[j]
        data[j]=tmp




class Test(unittest.TestCase):
    obj=Solution()
    def test_1(self):
        self.assertEqual(self.obj.inverse_pairs([7,5,6,4,10]), 5)

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
