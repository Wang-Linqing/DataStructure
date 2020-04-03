class Solution:
    stack=[]
    @staticmethod
    def permutation(string):
        if string is None:
            return
        Solution.stack.clear()
        Solution.permutation_str(string)

    @staticmethod
    def permutation_str(string):
        if len(string)==1:
            tmp=""
            for i in Solution.stack:
                tmp+=i
            tmp+=string[0]
            print(tmp)
            return
        for i in range(0,len(string)):
            Solution.stack.append(string[i])
            Solution.permutation_str(string[0:i]+string[i+1:])
            Solution.stack.pop()







string="abc"
Solution.permutation(string)