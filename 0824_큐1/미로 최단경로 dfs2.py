# 경로가 2개 이상인 미로에서 bfs 이용하여 경로 탐색 후
# 최단결로를 찾아보자
'''
3
5
11111
12001
10101
13001
11111
5
11111
12131
10111
10001
11111
9
111111111
120000001
101110101
100000101
111110101
101000101
101011101
100000031
111111111
'''
def dfs(i, j, s, N):
    global minV
    if maze[i][j] == 3:
        if minV > s + 1:
            minV = s + 1
        return
    else:
        visited[i][j] = 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if maze[ni][nj] != 1 and visited[ni][nj] == 0: # 벽으로 둘러쌓인 미로
                dfs(ni, nj, s+1, N)
        visited[i][j] = 0
        return
        
         
for tc in range(int(input())):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti = -1
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:             # 시작지점 좌표 구함
                sti, stj = i, j
                break
        if sti != -1:
            break
    answer = 0
    minV = N*N
    visited = [[0]*N for _ in range(N)]
    dfs(sti, stj, 0, N)
    if minV == N*N:
        minV = -1
    print(f'#{tc+1} {minV}')