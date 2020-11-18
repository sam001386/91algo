class Solution(object):
    def verticalTraversal(self, root):
        queue = collections.deque()
        queue.append((root, 0, 0))
        arr = []
        while queue:
            node, x, level = queue.popleft()
            arr.append((x, level, node.val))
                
            if node.left:
                queue.append((node.left, x - 1, level + 1))
            if node.right:
                queue.append((node.right, x + 1, level + 1))
        
        arr.sort(key = lambda x: (x[0], x[1], x[2]))
        seen = set()
        cur_res = []
        res = []
        for x, y, val in arr:
            if x not in seen:
                if cur_res:
                    res.append(cur_res)
                seen.add(x)
                cur_res = []
                cur_res.append(val)
            else:
                cur_res.append(val)
        
        res.append(cur_res)
        return res
