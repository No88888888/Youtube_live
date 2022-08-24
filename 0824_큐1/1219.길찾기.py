'''
그림과 같이 도식화한 지도에서 A도시에서 출발하여 B도시로 가는 길이 존재하는지 조사하려고 한다.

길 중간 중간에는 최대 2개의 갈림길이 존재하고, 모든 길은 일방 통행으로 되돌아오는 것이 불가능하다.

다음과 같이 길이 주어질 때, A도시에서 B도시로 가는 길이 존재하는지 알아내는 프로그램을 작성하여라.

 - A와 B는 숫자 0과 99으로 고정된다.

 - 모든 길은 순서쌍으로 나타내어진다. 위 예시에서 2번에서 출발 할 수 있는 길의 표현은 (2, 5), (2, 9)로 나타낼 수 있다.

 - 가는 길의 개수와 상관없이 한가지 길이라도 존재한다면 길이 존재하는 것이다.

 - 단 화살표 방향을 거슬러 돌아갈 수는 없다.



[제약 사항]

출발점은 0, 도착점은 99으로 표현된다.

정점(분기점)의 개수는 98개(출발점과 도착점 제외)를 넘어가지 않으며, 한 개의 정점에서 선택할 수 있는 길의 개수도 2개를 넘어가지 않는다.

아래 제시된 가이드 라인은 제안사항일 뿐 강제사항은 아니다.

[데이터 저장 가이드]

정점(분기점)의 개수가 최대 100개 이기 때문에, size [100]의 정적 배열 2개을 선언하여, 각 정점의 번호를 주소로 사용하고, 저장되는 데이터는 각 정점에서 도착하는 정점의 번호를 저장한다.

위 그림을 저장하였을 때 결과는 다음과 같다.
 


[입력]

각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호와 길의 총 개수가 주어지고 그 다음 줄에는 순서쌍이 주어진다.

순서쌍의 경우, 별도로 나누어 표현되는 것이 아니라 숫자의 나열이며, 나열된 순서대로 순서쌍을 이룬다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.
# '''
# dfs로 풀이

def dfs(v, N):
    top = -1
    visited[v] = 1
    while True:
        for w in adjList[v]:        # v위치에서 
            if visited[w] == 0:     # w가 방문하지 않은것이라면
                top += 1            # top 포인터 +1
                stack[top] = v      # stack 최상위에 v 저장
                v = w               # v를 w로 바꿈
                visited[w] = 1      # 새로방문한 W의 visited 1로 바꿔줌
                break
            if w == N:
                return 1            # 방문한 곳이 99라면 1로 반환
        else:                       # v위치에서 w가 없거나 다 방문했다면
            if top != -1:           # 그때 top이 -1이 아니라면
                v = stack[top]      # v를 이전 정점이었던 stack[top]으로 되돌림
                top -=1             
            else:                   # top이 -1이라면 출발지로 돌아온것
                return 0            # 0 반환
            
for tc in range(10):            
    T, E = map(int, input().split())        # TC의 넘버와 간선의 갯수 
    load = list(map(int, input().split()))  # 간선 쌍 리스트
    adjList = [[] for _ in range(100)]      

    for i in range(0, E*2, 2):              # 쌍으로 리스트 저장되어있기 때문에 E*2만큼 2칸씩
        adjList[load[i]].append(load[i+1])  # adjList[짝수번째 항]에 load[홀수번째항] 저장

    visited =[0]*100
    stack = [0]*100
    print(f'#{T} {dfs(0,99)}')

#-----------------------------------------------------------------------------------------

# bfs로 풀이

def bfs(v, N, t):                           # v 시작, N 마지막 정점, t 찾는 정점
    visited = [0] * (N+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        if v == t:                          # visited(v)
            return visited[99]              # 목표발견
        for w in adjList[v]:                # v에 인접하고 방문안한 w인큐, 표시
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
    return 0

for tc in range(10):             
    T, E = map(int, input().split())        # TC의 넘버와 간선의 갯수 
    arr = list(map(int, input().split()))   # 간선 쌍 리스트
    adjList = [[] for _ in range(100)]

    for i in range(E):
        a, b = arr[i*2], arr[i*2 + 1]
        adjList[a].append(b)                # 단방향


    bfs(0,99, 99)                           # 시작, 마지막, 목표 정점 