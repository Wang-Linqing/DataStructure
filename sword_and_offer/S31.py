class Solution:
    @staticmethod
    def is_pop_order(push_list,pop_list):
        stack=[]
        index=0
        for item in pop_list:
            if len(stack)==0:
                is_pop=False
                while index <len(push_list):
                    stack.append(push_list[index])
                    if stack[-1]==item:
                        stack.pop()
                        is_pop=True
                        break
                    else:
                        index+=1
                if is_pop:
                    pass
                else:
                    return False
            else:
                if item==stack[-1]:
                    stack.pop()
                else:
                    is_pop = False
                    while index < len(push_list):
                        stack.append(push_list[index])
                        if stack[-1] == item:
                            stack.pop()
                            is_pop = True
                            break
                        else:
                            index += 1
                    if is_pop:
                        pass
                    else:
                        return False
        return True
print(Solution.is_pop_order([1,2,3,4,5,6],[6,5,4,3,2,1]))
