class Solution:
    def plusOne(self,digits):
        carry = 1
        i = len(digits)-1
        
        while i >= 0:
            digits[i] += carry  # if 9 then will be converted to 10 [1,2,9] = [1,2,10]
            if digits[i] == 10: # if 10 then will run this condition [1,2,10]
                digits[i] = 0   # 10 will be converted to 0  [1,2,10] = [1,2,0]
                carry = 1       # carry will be 1
            
            else:               # if no 10
                carry = 0       # carry 0
                break 
            i -= 1     
        if carry:
            digits.insert(0, 1)
            
        return digits
    
    
solution = Solution()
testcase1 = [9,9]
testcase2 = [9,9,9]
testcase3 = [9,9,9,9]

print(solution.plusOne(testcase1))
print(solution.plusOne(testcase2))
print(solution.plusOne(testcase3))



        
    