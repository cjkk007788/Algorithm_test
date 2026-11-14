from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode | None) -> int:

        def Bfs(root):

            if root is None:
                return 0

            else:
                layer = 0
                q = deque()
                q.append(root)

                while(q):
                    layer = layer + 1
                    for _ in range(len(q)):
                        node = q.popleft()

                        if node.left is None and node.right is None:
                            return layer

                        if node.left is not None:
                            q.append(node.left)
                        if node.right is not None:
                            q.append(node.right)
                        
                return layer


        return Bfs(root)