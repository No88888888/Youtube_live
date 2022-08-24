def bfs(G, v):              # G: 그래프, v: 탐색의 시작점
    visited = [0] * (n + 1) # n : 정점의 갯수 
    queue = []
    queue.append(v)         # 시작점 v를 큐에 삽입
    
    while queue:
        t = queue.pop(0)    # 큐의 첫번재 원소를 반환
        if not visited[t]:  # 방문하지 않은 곳이라면
            visited[t] = True # 방문한 것으로 표시
            visited_action()  # 정점 t에서 할일 하기
        for i in G[t]:
            if not visited[i]:
                queue.append(i)