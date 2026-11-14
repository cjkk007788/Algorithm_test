# Definition for a binary tree node.
from collections import deque

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        left_q = deque()
        right_q = deque()
        left_tree = p
        right_tree = q

        left_q.append(left_tree)
        right_q.append(right_tree)

        while(left_q and right_q):
            
            left_tree = left_q.pop()    
            right_tree = right_q.pop()


            if(left_tree is None and right_tree is None):
                continue

            #구조가 다른 경우도 꼭 넣어야 했다.
            
            if(left_tree is None or right_tree is None or left_tree.val != right_tree.val):
                return False
            
            #None이라도 일단 넣는다. 위에서 한번에 해결한다.
            #None인 경우를 한 번에 해결
            #문제 풀기전에 공책에 그림을 그려서 어떤 식으로 비교해야할 지 먼저 생각하고
            #코딩하기
            left_q.append(left_tree.left)            
            right_q.append(right_tree.left)
            left_q.append(left_tree.right)
            right_q.append(right_tree.right)

        return True


        