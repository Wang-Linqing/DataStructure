class Solution:
    @staticmethod
    def binary_search(sorted_data,low,high,item):
        while low<=high:
            mid=(low+high)//2
            if sorted_data[mid]==item:
                return True,mid
            elif sorted_data[mid]>item:
                high=mid-1
            else:
                low=mid+1
        return False,high
sorted_data=[1,2,3,5,6,8,9,0]
print(Solution.binary_search(sorted_data,0,len(sorted_data)-1,7))


