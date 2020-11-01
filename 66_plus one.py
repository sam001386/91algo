class Solution(object):
    def plusOne(self, digits):
        carry = 0
        cur = 0
        res = []
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                if digits[i] + 1 == 10:
                    cur = 0
                    carry = 1 
                else:
                    cur = digits[i] + 1
                    carry = 0
            elif carry == 1 and digits[i] + 1 == 10:
                cur = 0
                carry = 1
            elif carry == 1:
                cur = digits[i] + 1
                carry = 0
            else:
                cur = digits[i]
            res.append(cur)

        if carry == 1:
            res.append(1)
        
        return res[::-1]
