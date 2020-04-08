import unittest


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Solution:
    def find_common_node(self, link_list_one, link_list_two):
        if link_list_one is None or link_list_two is None:
            return None
        p = link_list_one
        data = []
        while p is not None:
            data.append(p)
            p=p.next
        p = link_list_two
        while p is not None:
            if p in data:
                return p
            p=p.next
        return None


class Test(unittest.TestCase):
    obj = Solution()

    def test_1(self):
        a1 = Node(1)
        a2 = Node(2)
        a3 = Node(3)
        a4 = Node(4)
        a5 = Node(5)
        a6 = Node(6)
        a7 = Node(7)
        a1.next = a2
        a2.next = a3
        a3.next = a6
        a6.next = a7
        a4.next = a5
        a5.next = a6

        self.assertEqual(self.obj.find_common_node(a1, a4), a6)

    def test_2(self):
        self.assertEqual("", "")

    def test_3(self):
        self.assertEqual("", "")

    def test_4(self):
        self.assertEqual("", "")

    def test_5(self):
        self.assertEqual("", "")

    def test_6(self):
        self.assertEqual("", "")

    def test_7(self):
        self.assertEqual("", "")

    def test_8(self):
        self.assertEqual("", "")
