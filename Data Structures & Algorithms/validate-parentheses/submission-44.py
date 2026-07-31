class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        mapping={')':'(','}':'{',']':'['}
        stack=[]

        for n in s:
            if n not in mapping:
                stack.append(n)
                continue
            elif len(stack)>0:
                    c=stack.pop()
                    if mapping[n]!=c:
                        return False
            else:
                return False
        return len(stack) == 0