class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        if head is None:
            return
        if n < 1 :
            return
        
        nodelist = []
        cur = head

        while(cur):

            nodelist.append(cur)
            cur = cur.next

        size = len(nodelist)
        print(size)

        if n == size:

            head = head.next
        

        elif n == 1:
        
            nodelist[size-2].next =  None
        
        else:
        
            nodelist[size - n - 1].next = nodelist[size - n + 1]

        return head

class Solution2:
    def removeNthFromEnd(self,head:ListNode | None, n:int)->ListNode|None:

        dumy = ListNode(0,head)
        fast = slow = dumy

        #fast를 먼저 이동
        for _ in range(n):
            fast = fast.next

        #fast가 끝에 도달하면 삭제 대상은 slow next
        while fast.next : 
            fast = fast.next
            slow = slow.next

        slow = slow.next

        return dumy.next
    

        

def arrayTo_link(array):

    size = len(array)

    head = ListNode()
    cur = head
    for i in range(size):
        cur.next = ListNode(array[i])
        cur = cur.next

    return head.next

def printlist(ListNode):

    cur = ListNode

    while(cur):
        print(cur.val)
        cur = cur.next

    return

if __name__ == "__main__":

    list = [1,2]
    n = 1
    node = arrayTo_link(list)

    sol = Solution()

    node = sol.removeNthFromEnd(node,n)

    print("output")
    printlist(node)