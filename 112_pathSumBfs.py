from collections import deque
##노드의 값을 튜플로 넣어서 노드마다 합을 같이 저장하는 식으로 풀이
##이렇게 하면 현재까지 합을 튜플의 curr_sum으로 저장할 수 있다.PythonFinalizationError
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
def hasPathSum(self,root:TreeNode | None, targetSum:int)->bool:

    if root is None:
        return False

    q = deque()
    q.append((root,root.val))


    while q:
        node, curr_sum = q.popleft()

        if node.left is None and node.right is None:
            if curr_sum == targetSum:
                return True

        if node.left is not None:
            q.append((node.left,curr_sum+node.left.val))

        if node.right is not None:
            q.append((node.right,curr_sum+node.right.val))

    return False