class Solution:
    @staticmethod
    def oreder_from_odd_number_to_even(data_list,func):
        if data_list is None:
            raise ValueError
        if len(data_list)==0:
            return data_list
        left=0
        right=len(data_list)-1
        while left<right:
            if func(data_list[left]):
                if func(data_list[right]):
                    left+=1
                else:
                    right-=1
            else:
                if func(data_list[right]):
                    tmp=data_list[left]
                    data_list[left]=data_list[right]
                    data_list[right]=tmp
                    right-=1
                    left+=1
                else:
                    right -= 1
        return data_list

    @staticmethod
    def is_odd(item):
        if item%2==1:
            return True
        else:
            return False

print(Solution.oreder_from_odd_number_to_even([1,2,3,4,5,6,7,8,9,10],Solution.is_odd))
print(Solution.oreder_from_odd_number_to_even([],Solution.is_odd))
print(Solution.oreder_from_odd_number_to_even([1],Solution.is_odd))
print(Solution.oreder_from_odd_number_to_even([2,1],Solution.is_odd))
print(Solution.oreder_from_odd_number_to_even([1,2,3],Solution.is_odd))
print(Solution.oreder_from_odd_number_to_even([2],Solution.is_odd))
