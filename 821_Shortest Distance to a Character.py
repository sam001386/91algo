class Solution(object):
    def shortestToChar(self, S, C):
        res = [-1 for _ in range(len(S))]
        index = []
        for i in range(len(S)):
            if S[i] == C:
                res[i] = 0
                index.append(i)
        
        for i in range(1, len(index)):
            left = index[i - 1] + 1
            right = index[i] - 1
            cur = 1
            while left <= right:
                res[left] = cur
                res[right] = cur
                cur += 1 
                left += 1 
                right -= 1 
        
        if index[0] > 0:
            cur = 1
            for i in range(index[0] - 1, -1, -1):
                res[i] = cur
                cur += 1 
            
        if index[-1] < len(S) - 1:
            cur = 1
            for i in range(index[-1] + 1, len(S)):
                res[i] = cur
                cur += 1 
        
        return res
