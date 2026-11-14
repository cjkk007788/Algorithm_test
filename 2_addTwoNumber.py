class ListNode:
    def __init__(self, val=0, next=None):
        ##생성자
        ## cur = ListNode(a)
        ## 저절로 val에 a가 들어감 next도 지정가능
        self.val = val
        self.next = next

##자주 쓰이는 것들은 함수화 하기
# 연결리스트 조회할때는 next 쓰면서하기
# 연결 리스트를 만들때는 반복문 돌면서 노드를 생성하면서 가야함

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        #list to int
        def to_int(node):
            digits = []

            while(node):
                #node에 있는 val을 하나씩 꺼내서 append
                digits.append(str(node.val))
                node = node.next
                ##join을 쓰면 배열에 있는 숫자를 한번에 모아서 int로 변환
                #기억해두기
            return int("".join(digits[::-1]))


        total = to_int(l1) + to_int(l2)


        dummy = ListNode()
        cur = dummy
        #Build list
        #노드를 만들면서 추가하고 next로
        #cur이라는 변수 꼭 이용하기
        
        for ch in str(total)[::-1]:
            #Node를 생성하면서 연결
            cur.next = ListNode(int(ch))
            cur = cur.next
        #첫번째 dummy list에는 아무 것도 없음
        return dummy.next


def bulid_list(num:int):

    dummy = ListNode()

    cur = dummy
    ##역순으로 조회하는 코드
    for ch in str(num)[::-1]:
        #Node를 생성하면서 연결
        cur.next = ListNode(int(ch))
        cur = cur.next
    return dummy.next

def list_to_int(node:ListNode):

    digits = []

    while(node):

        digits.append(str(node.val))
        node = node.next
    return int("".join(digits[::-1]))


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (12, 34, 46),
        (34, 56, 90),
        (342, 465, 807),
        (0, 0, 0),
        (99, 1, 100),
    ]


    for num1, num2, expected in test_cases:
        result_node = sol.addTwoNumbers(bulid_list(num1),bulid_list(num2))

        result = list_to_int(result_node)

        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] {num1} + {num2} = {result} (expected {expected})")