class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        #항상 엣지 케이스, 없는 경우 바로 대비해두기
        if not strs:
            return

        first = strs[0]
        #count로 세면서 다 같을때까지하지말고 다른 순간 바로 빠져 나오도록 해라
        #그리고 인덱스가 있으면 어디까지 출력하는 식으로 구현하면 되니
        #새로운 메모리에 추가하지 않는다

        for k, ch in enumerate(first):
            #두번째 문자열 부터 본다
            for s in strs[1:]:
                if k >=len(s) or s[k] != ch:
                    return first[:k]
        return first

    


