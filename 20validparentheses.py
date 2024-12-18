class Solution:
    def isValid(self, s):
        stack = []
        closeToOpen = {')':'(',']':'[','}':'{'}
        
        for c in s:  #for characters in input
            if c in closeToOpen: #if characters in closetoopen
                if stack and stack[-1] == closeToOpen[c]:  #if key value pairs match
                    stack.pop()  #pop the following pairs
                else: 
                    return False
            else:
                stack.append(c)
        return True if not stack else False
    
    
solution=Solution()
s = '({})'
print(solution.isValid(s))