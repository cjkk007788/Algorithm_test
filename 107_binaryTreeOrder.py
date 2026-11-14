from collections import deque

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:

        def Bfs(root):

            if root is None:
                return []
            
            q = deque()

            q.append(root)
            result = []

            while(q):

                layer = []
                for _ in range(len(q)):
                    node = q.popleft()
                    layer.append(node.val)

                    if node.left is not None:
                        q.append(node.left)
                    if node.right is not None:
                        q.append(node.right)
            
                result.append(layer)
            
            result.reverse()

            return result

        return Bfs(root)

                
