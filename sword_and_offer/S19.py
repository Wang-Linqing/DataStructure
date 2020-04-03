import unittest


class Solution:
    @staticmethod
    def re(string, pattern):
        print(string, pattern)
        if string is None or pattern is None:
            return None
        length_str = len(string)
        length_pattern = len(pattern)
        if length_pattern==0 and length_str==0:
            return True
        if length_pattern==0 and length_str!=0:
            return False
        if pattern[0]==".":
            if length_str>=1:
                return Solution.re(string[1:length_str],pattern[1:length_pattern])
            else:
                return False
        elif length_pattern>=2 and pattern[1]=="*":
            if Solution.re(string,pattern[2:length_pattern]):
                return True
            else:
                if pattern[0]==string[0]:
                    return Solution.re(string[1:length_str],pattern)
                else:
                    return False
        else:
            if length_str<1:
                return False
            if pattern[0]==string[0]:
                return Solution.re(string[1:length_str],pattern[1:length_pattern])
            else:
                return False


class SolutionTest(unittest.TestCase):
    def test_7(self):
        self.assertEqual(Solution.re("", "b*"),True)
    def test_2(self):
        self.assertEqual(Solution.re("aaaaab", "a*a*.....b"), True)

    def test_1(self):
        self.assertEqual(Solution.re("baaa", "ba*a*"), True)

    def test_4(self):
        self.assertEqual(Solution.re("", "ba*a*"), False)

    def test_5(self):
        self.assertEqual(Solution.re("b", "ba*a*"), True)
    def test_6(self):
        self.assertEqual(Solution.re("", "b"),False)







if __name__ == "__main__":
    unittest.main()
