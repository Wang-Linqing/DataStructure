import unittest


class Solution:
    def get_first_k(self,data,k,start,end):
        if start>end:
            return -1
        mid=(start+end)//2
        if data[mid]==k:
            if mid ==0:
                return 0
            if data[mid-1]!=k:
                return mid
            return self.get_first_k(data,k,start,mid-1)
        elif data[mid]<k:
            return self.get_first_k(data,k,mid+1,end)
        else:
            return self.get_first_k(data,k,start,mid-1)
    def get_last_k(self,data,k,start,end):
        if start>end:
            return -1
        mid=(start+end)//2
        if data[mid]==k:
            if mid ==len(data)-1:
                return len(data)-1
            if data[mid+1]!=k:
                return mid
            return self.get_last_k(data,k,mid+1,end)
        elif data[mid]<k:
            return self.get_last_k(data,k,mid+1,end)
        else:
            return self.get_last_k(data,k,start,mid-1)
    def get_num_of_k(self,data,k):
        if data is None:
            return 0
        if len(data)==0:
            return 0
        first=self.get_first_k(data,k,0,len(data)-1)
        if first==-1:
            return 0
        last=self.get_last_k(data,k,0,len(data)-1)
        print(data,k,first,last)
        return last-first+1
    def get_missing_k(self,data):
        if data is None:
            return -1
        if len(data)==0:
            return -1
        if len(data)==1:
            if data[0]==0:
                return -1
            else:
                return 0
        start=0
        end=len(data)-1
        while start<=end:
            mid=(start+end)//2
            print(mid,data[mid])
            if data[mid]==mid:
                start=mid+1
            elif data[mid]>mid:
                if mid ==0:
                    return 0
                if data[mid-1]==mid-1:
                    return mid
                end=mid-1
            else:
                raise ValueError
        return -1
    def find_num_index_equal_value(self,data):
        if data is None:
            return -1
        if len(data)==0:
            return -1
        if len(data)==1:
            if data[0]==0:
                return 0
            else:
                return -1
        start=0
        end=len(data)-1
        while start<=end:
            mid=(start+end)//2
            if data[mid]==mid:
                return mid
            elif data[mid]<mid:
                start=mid+1
            else:
                end=mid-1
        return -1





class Test(unittest.TestCase):
    obj=Solution()
    def test_1(self):
        self.assertEqual(self.obj.get_num_of_k([1,2,3,4,4,4,4,4,5,6,7,8,9,9,10,10,10,11],10),3 )
        self.assertEqual(self.obj.get_num_of_k([1,2,3,4,4,4,4,4,5,6,7,8,9,9,10,10,10,11],4),5 )
        self.assertEqual(self.obj.get_num_of_k([1,2,3,4,4,4,4,4,5,6,7,8,9,9,10,10,10,11],15),0 )
        self.assertEqual(self.obj.get_num_of_k([1,2,3,4,4,4,4,4,5,6,7,8,9,9,10,10,10,11],11),1 )
        self.assertEqual(self.obj.get_num_of_k([1,2,3,4,4,4,4,4,5,6,7,8,9,9,10,10,10,11],1),1 )
        self.assertEqual(self.obj.get_num_of_k([1,2,3,4,4,4,4,4,5,6,7,8,9,9,10,10,10,11,13],12),0 )

    def test_2(self):
        self.assertEqual(self.obj.get_missing_k([0,2,3,4,5,6,7,8,9,10]), 1)
        self.assertEqual(self.obj.get_missing_k([0,1,2,3,4,5,7,8,9,10]), 6)
        self.assertEqual(self.obj.get_missing_k([0,1,2,3,4,5,6,7,8,9,10]), -1)

    def test_3(self):
        self.assertEqual(self.obj.find_num_index_equal_value([-3,-1,1,3,5]), 3)

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
