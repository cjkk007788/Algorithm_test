class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        def DFS(node,sum,targetSum):
            if node is None:
                return False

            sum = sum + node.val

            if node.left is None and node.right is None:
                return sum == targetSum
            
            return DFS(node.left,sum,targetSum) or DFS(node.right,sum,targetSum)

        return DFS(root,0,targetSum)