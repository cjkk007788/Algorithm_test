class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        dummy = ListNode()
        cur = dummy
        carry = 0

        #carry가 남아도 계속 하도록 하면 맨 마지막에 1을 넣을 수 있음
        #l1 None, l2 None, carry 0 이면 그만 돔
        #l1 None, l2 None, Carry 1 이면 마지막에 추가
        while(l1 or l2 or carry) :
            #l1이 존재하면 val 없으면 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total  = (v1 + v2 + carry)
            #몫을 구하는 것은 // 그냥 / --> 소수점 나옴
            carry = total // 10
            
            cur.next = ListNode(total % 10)
            cur = cur.next
            if l1 :
                l1 = l1.next
            if l2 :
                l2 = l2.next
        return dummy.next

def build_list(num:int)-> ListNode:

    dummy = ListNode()
    cur = dummy
    for ch in str(num)[::-1]:
        cur.next = ListNode(int(ch))
        cur = cur.next

    return dummy.next

def list_to_int(node:ListNode):
    digits = []

    while(node):
        digits.append(str(node.val))
        node = node.next

    return int("".join(digits)[::-1])
        
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (12, 34, 46),
        (34, 56, 90),
        (342, 465, 807),
        (0, 0, 0),
        (99, 1, 100),          # 마지막 carry 처리 확인
        (9999999, 9999, 10009998),  # 길이가 다른 경우
    ]

    for num1, num2, expected in test_cases:
        result_node = sol.addTwoNumbers(build_list(num1), build_list(num2))
        result = list_to_int(result_node)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] {num1} + {num2} = {result} (expected {expected})")