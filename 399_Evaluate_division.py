from typing import List
import heapq
import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

            def buildGraph(self, equations, values):
                graph = collections.defaultdict(dict)

                for (start,end),weight in zip(equations,values):
                    graph[start][end] = weight
                    graph[end][start] = 1/weight
                
                return graph

            def dfs(self,start,end,visited,graph):

                if start not in graph and end not in graph:
                    return -1.0

                if end in graph[start]:
                    return graph[start][end]
                
                visited.add(start)

                for neighbor,weight in graph[start].items():
                    if neighbor not in visited:
                        cumlativeweight = self.dfs(neighbor,end,visited,graph)
                        if(cumlativeweight != -1.0):
                            return weight * cumlativeweight
                
                return -1.0

            result = []
            
            graph = self.buildGraph(equations,values)

            for start,end in queries:
                result.append(self.dfs(start,end,set(),graph))

            return result
                