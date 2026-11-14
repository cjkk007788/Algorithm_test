# Definition for a binary tree node.
import Study.DFS
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque

class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def dfs(node,depth):
            nonlocal max_depth
            if(node is None):
                return

            if(depth>max_depth):
                max_depth = depth
    
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
            
        dfs(root,1)

        return max_depth
    ##Divide and conquer 방식
    def maxDepth_DFS(self, root: Optional[TreeNode]):
        
        if root is None:
            return 0

        #트리의 최대 깊이는 1+max(왼쪽 서브트리 깊이, 오른쪽 서브트리 깊이)

        left = self.maxDepth_DFS(root.left)
        right = self.maxDepth_DFS(root.right)

        return 1 + max(left,right)
    def maxDepth_BFS(self, root: Optional[TreeNode]) -> int:
    
        if not root:
            return 0

        queue = deque()
        queue.append(root)

        while(queue):
            #while 한 바퀴가 층이 된다.
            
            for _ in range(len(queue)):
                node = queue.popleft()
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            depth = depth + 1

        return depth

            
            
            