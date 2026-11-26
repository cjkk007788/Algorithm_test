# Definition for singly-linked list.
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
    