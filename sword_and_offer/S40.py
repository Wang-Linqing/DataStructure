import unittest
import random


class Solution:
    def find_min_k_mun(self,data, k):
        if data is None:
            return None
        if len(data) <= 0:
            return None
        if k <= 0 or k > len(data):
            return None
        index = self.partition(data, 0, len(data) - 1)
        start = 0
        end = len(data) - 1
        while index != k - 1:
            if index > k - 1:
                end = index - 1
                index = self.partition(data, start, end)
            else:
                start = index + 1
                index = self.partition(data, start, end)
        self.quick_sort(data[0:k], 0, k - 1)
        data.sort()
        return data[0:k]

    def partition(self,data: list, start: int, end: int):
        if data is None or len(data) <= 0 or start < 0 or end >= len(data) or start > end:
            raise ValueError
        if start==end:
            index=start
        else:
            index = random.randrange(start,end)
        tmp = data[end]
        data[end] = data[index]
        data[index] = tmp
        small = start - 1
        for i in range(start, end):
            if data[i] < data[end]:
                small += 1
                if i != small:
                    tmp = data[small]
                    data[small] = data[i]
                    data[i] = tmp
        small += 1
        tmp = data[small]
        data[small] = data[end]
        data[end] = tmp
        return small

    def quick_sort(self,data: list, start: int, end: int) -> list:
        if start == end:
            return
        index = self.partition(data, start, end)
        if index > start:
            self.quick_sort(data, start, index - 1)
        if index < end:
            self.quick_sort(data, index + 1, end)


class Test(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        data = [23, 45, 123, 1, 234, 3, 5, 8]
        self.assertListEqual(self.obj.find_min_k_mun(data, 2), [1, 3])

    def test_2(self):
        data = [1]
        self.assertListEqual(self.obj.find_min_k_mun(data, 1), [1])

    def test_3(self):
        data = [1,2]
        self.assertListEqual(self.obj.find_min_k_mun(data, 1), [1])

    def test_4(self):
        data = [2,1]
        self.assertListEqual(self.obj.find_min_k_mun(data, 1), [1])

