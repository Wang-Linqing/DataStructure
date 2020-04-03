import random


class Solution:
    @staticmethod
    def swap(data: list, index1: int, index2: int):
        tmp = data[index1]
        data[index1] = data[index2]
        data[index2] = tmp

    @staticmethod
    def partition(data: list, start: int, end: int):
        print("in",data)
        length = len(data)
        if length <= 0 or start < 0 or end >= length or end < start:
            print(start,end)
            raise ValueError
        index = random.randrange(start, end)
        Solution.swap(data, index, end)
        small = start - 1
        for i in range(start, end):
            if data[i] < data[end]:
                small += 1
                if small != i:
                    Solution.swap(data, small, i)
        small += 1
        Solution.swap(data,small, end)
        print("out",data,small)
        return small

    @staticmethod
    def quick_sort(data: list, start: int, end: int) -> list:
        if start == end:
            return
        index = Solution.partition(data, start, end)
        if index > start:
            Solution.quick_sort(data, start, index - 1)
        if index < end:
            Solution.quick_sort(data, index + 1, end)


data = [12, 1, 3, 78, 98, 32, 45, 213, 12, 34, 56, 12, 345, 13]
print(data)
Solution.quick_sort(data, 0, len(data)-1)
print(data)

