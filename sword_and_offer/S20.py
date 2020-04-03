

class Solution:
    @staticmethod
    def is_digital(string):
        index=0
        while index <len(string):
            if string[index]=="e" or string[index]=="E":
                break
            else:
                index+=1
        if index<len(string):
            return (Solution.is_decimal(string[0:index]) or Solution.is_integer(string[0:index])) and Solution.is_integer(string[index+1:])
        else:
            return (Solution.is_decimal(string[0:index]) or Solution.is_integer(string[0:index]))
    @staticmethod
    def is_decimal(string):
        if string is None:
            return False
        if len(string)==0:
            return False
        if string[0]=="+" or string[0]=="-":
            return Solution.is_unsigned_decimal(string[1:])
        else:
            return Solution.is_unsigned_decimal(string)
    @staticmethod
    def is_unsigned_decimal(string):
        if string is None:
            return False
        if len(string)<2:
            return False
        index_dot=0
        while index_dot<len(string):
            if string[index_dot]==".":
                break
            else:
                index_dot+=1
        if index_dot==len(string):
            return False
        if index_dot==0:
            return Solution.is_mun(string[1:])
        elif index_dot==1:
            if Solution.is_mun(string[0]):
                if len(string)-2>0:
                    return Solution.is_mun(string[2:])
                else:
                    return True
            else:
                return False
        else:
            if Solution.is_unsigned_integer(string[0:index_dot]):
                if len(string)-index_dot==1:
                    return True
                else:
                    return Solution.is_mun(string[index_dot+1:])
            else:
                return False





    @staticmethod
    def is_integer(string):
        if string is None:
            return False
        if len(string)==0:
            return False
        if string[0]=="+" or string[0]=="-":
            return Solution.is_unsigned_integer(string[1:])
        else:
            return Solution.is_unsigned_integer(string)
    @staticmethod
    def is_unsigned_integer(string):
        if string is None:
            return False
        if len(string)==0:
            return False
        elif len(string)==1:
            if string[0]>="0" and string[0]<="9":
                return True
            else:
                return False
        else:
            if string[0]=="0":
                return False
            else:
                return Solution.is_mun(string)
    @staticmethod
    def is_mun(string):
        if string is None:
            return False
        if len(string)==0:
            return False
        index=0
        while index <len(string):
            if string[index]>="0" and string[index]<="9":
                index+=1
            else:
                return False
        if index==len(string):
            return True
        else:
            return False

print(Solution.is_digital("0.2"))
print(Solution.is_digital("0."))
print(Solution.is_digital(".0"))
print(Solution.is_digital("-.1"))
print(Solution.is_digital("-.0"))
print(Solution.is_digital("-.0E+2"))
print(Solution.is_digital("-.0e-2"))
print(Solution.is_digital("9342.02134E324"))
print(Solution.is_digital("+9342.02134E324"))
print(Solution.is_digital("+9342.02134E-324"))
print(Solution.is_digital("+.02134E-324"))
print(Solution.is_digital(""))











