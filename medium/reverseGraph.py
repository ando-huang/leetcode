#faster than 100% of python sols

class Solution:
    def solve(self, graph):
        revGraph = [[] for i in range(len(graph))]
        for i in range(len(graph)):
            for nbh in graph[i]:
                revGraph[nbh].append(i)
        return revGraph
