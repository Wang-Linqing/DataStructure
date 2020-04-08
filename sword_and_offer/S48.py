import unittest


class Solution:
    def longest_substring_without_duplication(self,string):
        if string is None:
            return 0
        if len(string)==0:
            return 0
        if len(string)==1:
            return 1
        max_count=1
        end=0
        start=0
        while end<len(string)-1:
            substring=string[start:end+1]
            new_char=string[end+1]
            print(substring,new_char)
            if new_char in substring:

                index=substring.index(new_char)
                start=start+index+1
                end+=1
                print(start,end)
            else:
                end+=1
            length=end-start+1
            max_count=max(length,max_count)
        return max_count





class Test(unittest.TestCase):
    obj=Solution()
    def test_1(self):
        self.assertEqual(self.obj.longest_substring_without_duplication("abcdbf"),4 )
        self.assertEqual(self.obj.longest_substring_without_duplication(""),0 )
        self.assertEqual(self.obj.longest_substring_without_duplication(None),0 )
        self.assertEqual(self.obj.longest_substring_without_duplication("a"),1 )
        self.assertEqual(self.obj.longest_substring_without_duplication("aaaaabbbbb"),2)





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
