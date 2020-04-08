import unittest


class Solution:
    def find_num_in_sequence(self,n):
        if n is None:
            return -1
        if n <= 9:
            return str(n)
        count=1
        print("n",n)
        n+=1
        while True:
            tmp=self.rest_n(count)
            if n>tmp:
                n=n-tmp
                count+=1
            else:
                n=n-1
                _count=n//count
                _rest=n%count
                data=pow(10,count-1)+_count
                data=str(data)
                print("n:",n,"_count:",_count,"_rest",_rest,"data",data,"data[]",data[_rest])
                return data[_rest]


    def rest_n(self,length):
        if length==1:
            return 10
        else:
            return length*9*pow(10,length-1)




class Test(unittest.TestCase):
    obj=Solution()
    def test_1(self):
        self.assertEqual(self.obj.find_num_in_sequence(10),"1")
        self.assertEqual(self.obj.find_num_in_sequence(190),"1")
        self.assertEqual(self.obj.find_num_in_sequence(189),"9")
        self.assertEqual(self.obj.find_num_in_sequence(2889),"9")

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
