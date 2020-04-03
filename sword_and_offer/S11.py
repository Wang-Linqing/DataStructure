class Solution(object):
    @staticmethod
    def get_min(data):
        if data is None:
            return None
        if len(data)==0:
            return None
        if len(data)==1:
            return data[0]
        l=0
        h=len(data)-1
        mid=0
        while data[l]>=data[h]:
            if h-l==1:
                mid=h
                break
            mid=(l+h)//2
            if data[l]==data[h] and data[l]==data[mid]:
                return Solution.min_in_order(data,l,h)
            if data[mid]<=data[h]:
                h=mid
            elif data[mid]>=data[l]:
                l=mid
        return data[mid]
    @staticmethod
    def min_in_order(data,l,h):
        result=data[l]
        for i in range(l,h+1):
            if data[i]<result:
                result=data[i]
        return result

print(Solution.get_min([1,-1,-1]))

