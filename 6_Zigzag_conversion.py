class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ##예외처리 꼭 해주기
        if numRows == 1 or numRows >= len(s):
            return s

        length = len(s)
        jump_const = 2*numRows-2
        ##올림식
        iteration = (length + jump_const -1) // (jump_const)
        result = []

        ##반복문에는 iterble한게 들어가야해서 정수를 쓰면 안된다
        ##행 과 열의 순서를 바꾸면 들어가는 순서가 바뀐다.
        #읽는 순서와 행렬의 순서를 일치시키자
        
        for i in range(1,numRows+1):
            for k in range(iteration):
                idx = i + jump_const* k -1
                if idx< length:
                    result.append(s[idx])
                if(i !=1 and i != numRows):
                    diag = jump_const*(k+1) - i + 1
                    if diag < length:
                        result.append(s[diag])
        return "".join(result)
