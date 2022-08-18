def dfs(v):

    
    print(v)            # 방문
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0: #방문하지 않은 w
            dfs(w)


V, E = map(int, input().split()) # V=6 E=8
N = V + 1 # N: 7
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N   # visited 생성
stack = [0] * N     # stack 생성
dfs(0, N)
