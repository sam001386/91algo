'''
思路：

很有趣的问题，有点像encoding and decoding，序列化的方式有很多
序列化：
使用BFS，这里注意需要存储None为“#“，并且再数组末尾将多余的None移除 (移除的是最后一行叶子节点相连的None)
将样例中的二叉树序列化成：[“1”,“2”,“3”,“#”,“#”,“4”,"5"], 再转化成字符串
反序列化：
把字符串转成数组，使用BFS，从上到下每层添加逐次添加相应元素，碰到“#”(None)则跳过，最后返回root即可
'''
class Codec:
    def serialize(self, root):
        if not root:
            return ""
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            cur = queue.popleft()
            if cur:
                res.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                res.append("#")
        while res[-1] == "#":
            res.pop()
        return ','.join(res)
        
    def deserialize(self, data):
        if not len(data):
            return None
        data = data.split(",")
        root = TreeNode(int(data[0]))
        index = 1 
        queue = collections.deque()
        queue.append(root)
        while queue:
            cur = queue.popleft()
            if index <= len(data) - 1 and data[index] != "#":
                cur.left = TreeNode(int(data[index]))
                queue.append(cur.left)
            index += 1 
            if index <= len(data) - 1 and data[index] != "#":
                cur.right = TreeNode(int(data[index]))
                queue.append(cur.right)
            index += 1
        return root 
