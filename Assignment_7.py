"""
Assignment 07

Team members:
1. Shubham Gupta
2. Prerna Choudhary
3. Irina Kuzmitskaya
4. Abhijeet Shekhar
5. Samiuddin Syed
"""

#using tarjan algorithm
def routersConnectedAllTime(numRouters, numLinks, links):
    n = numRouters + 1
    graph = [[] for _ in range(n)]

    #generate graph for list links
    for x, y in links:
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * n
    low = [None] * n
    time = [None] * n
    t = [0]
    res = []

    def dfs(node, parent=None):
        visited[node] = True
        low[node] = time[node] = t[0]
        t[0] += 1

        for aRouter in graph[node]:
            if parent == aRouter:
                continue
            if visited[aRouter]:
                low[node] = min(low[node], time[aRouter])
            else:
                dfs(aRouter, node)
                low[node] = min(low[node], low[aRouter])

                if low[aRouter] > time[node]:
                    res.append(node)

    for i in range(n):
        if visited[i] == False:
            dfs(i)

    res.sort()
    return res


numRouters = 7
numLinks = 7
links = [[1, 2], [1, 3], [2, 4], [3, 4], [3, 6], [6, 7], [4, 5]]
output = routersConnectedAllTime(numRouters, numLinks, links)

print("Output = ", output)