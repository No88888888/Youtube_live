def bfs(N):
    visited = [[0]*N for _ in range(N)]
    q = []
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2: 
                q.append((i,j))
                visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        # if maze[i][j] == 3:     # 3번인지 확인
        #     return visited[i][j]
        
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<ni<N and 0<=nj<N and maze[ni][nj] !=1 and visited[ni][nj] ==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return
         
for tc in range(int(input())):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    bfs(N)
    # sti = -1
    # stj = -1
    # for i in range(N):
    #     for j in range(N):
    #         if maze[i][j] == 2:             # 시작지점 좌표 구함
    #             sti, stj = i, j
    #             break
    #     if sti != -1:
    #         break
            
    print(f'#{tc+1} {bfs(N)}')