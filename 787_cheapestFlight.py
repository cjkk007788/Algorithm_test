import collections
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for start,end,price in flights:
            graph[start].append((end,price))

        INF = float('inf')
        cost = [INF] * n

        # DFS를 위한 가지치기(메모이제이션) 딕셔너리
        memo = {}

        def findWay_dfs(current, dst, k, stop, current_cost):

            if stop > k+1:
                return

            if current_cost >= cost[dst]:
                return

            if current == dst:
                cost[dst] = current_cost
                return

            # 동일한 노드에 동일한 횟수로 방문했을 때 기존보다 비용이 크거나 같으면 가지치기 (LeetCode TLE 방지)
            # 메모이제이션을 통한 가지치기로 효율 극대화 하는 방법
            if current_cost > memo.get((current,stop),INF):
                return
            memo[(current,stop)] = current_cost
            

            for neighbor,weight in graph[current]:
                findWay_dfs(neighbor,dst,k,stop+1,current_cost+weight)

            return cost[dst]
        # self. 은 내부 함수이므로 제거합니다. 반환값을 사용할 필요 없이 전역/외부 변수 cost[dst]를 갱신합니다.
        result = findWay_dfs(src,dst,k,0,0)
        
        
        return result


if __name__ == "__main__":
    solution = Solution()
    n = 5
    flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
    src = 0
    dst = 2
    k = 2
    
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    print(f"검증 결과 (가장 저렴한 가격): {result}")
