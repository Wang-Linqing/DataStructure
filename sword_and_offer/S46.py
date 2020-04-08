import unittest


class Solution:
    def get_count(self,num:int):
        if num is None:
            return 0
        if num<0:
            return 0
        data=str(num)
        return self.__get_count(data)
    def __get_count(self,str_num:str):
        print(str_num)
        if len(str_num)==0:
            return 0
        elif len(str_num)==1:
            return 1
        counts=[0 for _ in range(len(str_num))]
        count=0
        for i in range(0,len(str_num)):
            index=len(str_num)-i-1
            print(index)
            if index<len(str_num)-1:
                count=counts[index+1]
            else:
                count=1
            if index<len(str_num)-1:
                digit1=str_num[index]
                digit2=str_num[index+1]
                int_data=int(digit1+digit2,10)
                if int_data>=10 and int_data<=25:
                    if index<len(str_num)-2:
                        print("index",index)
                        count+=counts[index+2]
                    else:
                        count+=1
            counts[index]=count
        print(counts)
        count=counts[0]
        return count




class Test(unittest.TestCase):
    obj=Solution()
    def test_1(self):
        self.assertEqual(self.obj.get_count(123), 3)

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
