# Definition for singly-linked list.
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        def merge_two_list(list1 : ListNode, list2 : ListNode):

            dummy= ListNode()
            cur =dummy

            while(list1 and list2):
                
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next

                cur = cur.next
            cur.next = list1 if list1 else list2

            return dummy.next
        

        if not lists:
            return None

        n = len(lists)

        dynamic_merge = lists[0]

        for i in range(n-1):
            dynamic_merge = merge_two_list(dynamic_merge,lists[i+1])

        return dynamic_merge
            

#맨 앞자리에 있는걸 계속 비교하는 알고리즘
#heap에다가 넣었다가 빼는 연산
#위의 방법은 순차 비교를 하기 때문에 느리다
#이 방법은 힙에다가 넣어다가 빼는 연산이 Log k라 빠르다

class Solution2:
    def mergeKLists(self,lists:list[ListNode | None]) -> ListNode | None:
        heap = []

        for i, node in enumerate(lists):
            if node:
                #node val 기준으로 heap push
                heapq.heappush(heap,(node.val,i,node))

        dummy = ListNode()
        cur = dummy

        while(heap):
            val,i,node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next))

        return dummy.next


#Soultion 1은 개수가 순차적으로 줄어서 라운드 수가 n
#Soultion 3은 개수가 2배씩 줄어서 라운드수가 Log n
class Solution3:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        def merge_two_list(l1, l2):
            dummy = ListNode()
            cur = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2
            return dummy.next

        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(merge_two_list(l1, l2))
            lists = merged

        return lists[0]


def list_to_link(list):

    n = len(list)

    head = ListNode()
    cur = head
    for i in range(n):
        node = ListNode(list[i])
        cur.next = node
        cur = cur.next

    return head.next

def print_link(head):

    cur = head
    while(cur):
        print(cur.val)
        cur = cur.next

    return 0

if __name__ == "__main__":

    list1 = [1,4,5,6]
    list2 = [2,3,4,7]
    list3 = [1,4,5,10,11]

    head1 = list_to_link(list1)
    head2 = list_to_link(list2)
    head3 = list_to_link(list3)
    print("head1")
    print_link(head1)
    print("head2")
    print_link(head2)

    sol = Solution()

    sample_merge = sol.mergeKLists([head1,head2,head3])

    print("sample merge")
    print_link(sample_merge)
    