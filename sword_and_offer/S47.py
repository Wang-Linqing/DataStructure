import unittest


class Solution:
    def find_max_present_value(self,data:list):
        if data is None:
            return 0
        if len(data)==0:
            return 0
        if data[0] is None:
            return 0
        if len(data[0])==0:
            return 0
        return self.traverse(data,0,0)
    def traverse(self,data,row,col):
        rows=len(data)
        cols=len(data[0])
        if row==rows-1 and col==cols-1:
            return data[row][col]
        if row+1<=rows-1:
            if col+1<=cols-1:
                right=data[row][col]+self.traverse(data,row,col+1)
                down = data[row][col] + self.traverse(data, row + 1,col)
                return max(right,down)
            else:
                down=data[row][col]+self.traverse(data,row+1,col)
                return down
        elif row ==rows-1:
            right = data[row][col] + self.traverse(data, row, col + 1)
            return right


class Test(unittest.TestCase):
    S=[[1,10,3,8],[12,2,9,6],[5,7,4,11],[3,7,16,5]]
    obj=Solution()
    def test_1(self):
        self.assertEqual(self.obj.find_max_present_value(self.S), 53)

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
