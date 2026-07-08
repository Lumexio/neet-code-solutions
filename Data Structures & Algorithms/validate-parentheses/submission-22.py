class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <2: return False
        op={']':'[',')':'(','}':'{'}
        stack=list()
        for l in s:
            if l not in op:
                stack.append(l)
                print(l,stack)
            else:
                if len(stack)>0:
                    if op[l] !=stack.pop(): return False
                else: return False
        if len(stack)>0:return False
        else: return True