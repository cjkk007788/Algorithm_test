class Soultion1:
    def convert(self,s:str,numRows:int)->str:
        #예외처리는 직관적으로 해라
        #길이 넘어가면 안되겠지
        #1이면 그냥 출력
        #함수의 맨처음에 예외처리를 하는 게좋다 (입력에 대한 예외처리)
        if numRows == 1 or numRows >=len(s):
            return s

        #자주 쓰이는 상수를 만들어두기

        length = len(s)
        cycle = 2 * numRows -2
        result = []

        #정답의 읽는 순서와 행렬의 넣는 순서를 잘 일치시키기

        for r in range(numRows):
            for base in range(0,length,cycle):
                #처음과 끝만 넣게되는 것
                if base + r < length:
                    result.append(s[base+r])

                if 0 < r < numRows-1:
                    diag = base + cycle - r
                    if diag < length:
                        result.append(s[diag])

        return "".join(result)


##시뮬레이션 기법
## 움직이는 방향을 정해서 가기
class Solution2:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        #행마다 문자열 (2 by 2를 전체 크기로 만들지 않고 하나씩 추가해서 메모리 과열 없이 함)  
        rows =[""]*numRows
        #다이나믹하게 프로그래밍
        r, step = 0,1
        #문자열을 돌면서 r 과 step을 체크
        for ch in s:
            #r번째행에 append
            rows[r] += ch
            if r == 0:
                step = 1
            elif r == numRows -1:
                step = -1
            else:
                r = r+step
        #2차원 rows를 위에서 부터 합침
        return "".join(rows)
        
