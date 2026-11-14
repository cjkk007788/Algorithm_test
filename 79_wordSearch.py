from typing import List

#all direction

def exist(board: List[List[str]], word: str) -> bool:
    index = 0

    ROWS,COLS = len(board), len(board[0])
    visited = [[False]*COLS for _ in range(ROWS)]
    #리스트 크기 만큼 2중반복문 돌며

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    def Dfs(board: List[List[str]],word: str,x: int,y: int,visited: List[List[bool]],index: int) -> bool:
        if x<0 or y<0 or x>=len(board) or y>=len(board[0]):
            return False

        if visited[x][y] or board[x][y] != word[index]:
            return False

        if index == len(word)-1:
            return True

        #조건 다 충족되면 visit    
        visited[x][y] = True
        for i in range(4):
            if(Dfs(board,word,x+dx[i],y+dy[i],visited,index+1)):
                return True

        #back tracking 하는 부분
        visited[x][y] = False
        return False

    for i in range(len(board)):
        for j in range(len(board[i])):
            #if dfs return true --> return true until the last one recursion
            if(Dfs(board,word,i,j,visited,index)):
                return True
    return False
    #BFS호출
