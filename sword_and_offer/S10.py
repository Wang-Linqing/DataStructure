class Solution:
    @staticmethod
    def f(n):
        if n==0:
            return 0
        if n==1:
            return 1
        zero=0
        one=1
        n_1=1
        n_2=0
        for i in range(0,n-1):
            result=n_1+n_2
            n_2=n_1
            n_1=result

        return result
print(Solution.f(7))
