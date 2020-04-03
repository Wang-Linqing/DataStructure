# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers is None:
            return 0
        if len(numbers) == 0:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        if len(numbers) == 2:
            if numbers[0] == numbers[1]:
                return numbers[0]
            else:
                return 0
        length = len(numbers)
        index = 0
        start = 0
        end = length - 1
        while index != length // 2:
            if index > length // 2:
                end = index - 1
                if start < end:
                    index = self.partition(numbers, start, end)
                else:
                    return 0
            else:
                start = index + 1
                if start < end:
                    index = self.partition(numbers, start, end)
                else:
                    return 0
        return Solution.check(numbers, index)

    def partition(self, data, start, end):
        if len(data) <= 0 or start < 0 or end >= len(data) or end <= start:
            raise ValueError
        index = start
        tmp = data[end]
        data[end] = data[index]
        data[index] = tmp
        small = start - 1
        for i in range(start, end):
            if data[i] < data[end]:
                small += 1
                if i != small:
                    tmp = data[i]
                    data[i] = data[small]
                    data[small] = tmp
        small += 1
        tmp = data[small]
        data[small] = data[end]
        data[end] = tmp
        return small

    @staticmethod
    def check(_data, index):
        count = 0
        for i in _data:
            if i == _data[index]:
                count += 1
        if count > len(_data) - count:
            return _data[index]
        else:
            return 0


data = [1, 2, 3, 2, 4, 2, 5, 2, 3]
print(data)
obj = Solution()
ret = obj.MoreThanHalfNum_Solution(data)
print(ret)
