class Solution():
    @staticmethod
    def print_1_to_n_digits(n):
        if n<1:
            raise ValueError
        tmp=1
        max=1
        while tmp<=n:
            max=max*10
            tmp+=1
        max = max-1
        tmp=1
        while tmp<=max:
            print(tmp)
            tmp+=1

Solution.print_1_to_n_digits(44)