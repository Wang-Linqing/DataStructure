class Solution:
    @staticmethod
    def cut_string(n):
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        products = []
        products.append(0)
        products.append(1)
        products.append(2)
        products.append(3)
        max = 0
        for i in range(4, n + 1):
            max = 0
            for j in range(1, i // 2 + 1):

                profuct = products[j] * products[i - j]
                print(i, j, i - j, profuct)
                if profuct > max:
                    max = profuct
            products.append(max)
        max = products[n]
        print(products)
        return max

    @staticmethod
    def cut_string_tan_lan(n):
        if n < 2:
            return 0
        if n==2:
            return 1
        if n==3:
            return 2
        time_of_3=n//3
        if n-time_of_3*3==1:
            time_of_3-=1
        time_of_2=(n-time_of_3*3)//2
        return pow(3,time_of_3)*pow(2,time_of_2)

a=100
print(Solution.cut_string(a),Solution.cut_string_tan_lan(a))
