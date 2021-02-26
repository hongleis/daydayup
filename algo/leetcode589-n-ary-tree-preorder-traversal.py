# 给定一个 N 叉树，返回其节点值的前序遍历。
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# 递归，简单
class Solution1:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def pre(r):
            if not r:
                return
            res.append(r.val)
            for i in range(len(r.children)):
                pre(r.children[i])
        pre(root)
        return res

# 迭代，需要用到栈
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return []
        stack = [root]
        while(stack):
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children[::-1])

        return res