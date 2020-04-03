class Solution:
    @staticmethod
    def power(x,exponent):
        if x==0 and exponent<0:
            raise ValueError
        if exponent==0:
            return 1

        if exponent>=0:
            return Solution.pow_positive_e(x,exponent)
        else:
            return 1.0/(Solution.pow_positive_e(x,-exponent))

    @staticmethod
    def pow_positive_e(x,exponent):
        if exponent>=0:
            if exponent==0:
                return 1
            else:
                if exponent==1:
                    return x
                times=exponent//2
                tmp=x
                for i in range(0,times):
                    tmp=tmp*tmp
                if exponent%2==1:
                    return tmp*x
                else:
                    return tmp
        else:
            raise ValueError

print(Solution.power(2,3))
print(Solution.power(-2,-3))
print(Solution.power(-2,4))
print(Solution.power(2,0))
print(Solution.power(0,3))
from decimal import Context
print(0.1-0.100000000000000001<=0.000000001)