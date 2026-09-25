class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        cache = {'}':'{', ']':'[', ')':'('}

        for b in s:
            if b in cache:
                if stack and stack[-1] == cache[b]: 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)


        return len(stack) == 0