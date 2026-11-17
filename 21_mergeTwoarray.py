class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        result = ListNode()
        cur = result
        while(list1 or list2):
            if(list1 != None and list2 != None):
                if(list1.val >= list2.val):
                    nextnode = ListNode(list2.val)
                    cur.next= nextnode
                    cur = cur.next
                    list2 = list2.next
                else:
                    nextnode = ListNode(list1.val)
                    cur.next = nextnode
                    cur = cur.next
                    list1 = list1.next
            else:
                if(list1!=None):
                    while(list1):
                        nextnode = ListNode(list1.val)
                        cur.next = nextnode
                        cur = cur.next
                        list1 = list1.next
                else:
                    while(list2):
                        nextnode = ListNode(list2.val)
                        cur.next = nextnode
                        cur = cur.next
                        list2 = list2.next
        return result.next

def make_testlist(array):

    list = ListNode()
    size = len(array)

    cur = list
    for i in range(size):
        cur.val = array[i]
        print(f"{cur.val}")
        nextnode = ListNode()
        if(i != size-1):
            cur.next = nextnode
            cur= cur.next
    return list

def printlist(ListNode):

    cur = ListNode

    while(cur):
        print(cur.val)
        cur = cur.next

    return



class solution2:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            
            cur = cur.next

        cur.next = list1 or list2
        return dummy.next


def make_testlist2(array):

    dummy = ListNode()
    cur = dummy

    for v in array:

        cur.next = ListNode(v)
        cur = cur.next

    return dummy

def printlist2(head):


    vals = []

    while head:
        vals.append(head.val)
        head = head.next

    print(vals)

if __name__ == "__main__":

    array1 = [1,2,4]
    array2 = [1,3,4]

    list1 = make_testlist(array1)
    list2 = make_testlist(array2)

    sol = Solution()

    print("list1")
    printlist(list1)
    print("list2")
    printlist(list2)

    result = sol.mergeTwoLists(list1,list2)

    print("result")
    printlist(result)

    
    
