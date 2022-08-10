N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

#우하향 대각선 합

s = 0
for i in range(N):
    for j in range(N):
        if i==j:
            s += arr[i][j]

# 변수 i 하나 쓴 버전
s= 0
for i in range(N):
    s += arr[i][i]

# 역 대각선 버전
s = 0
for i in range(N):
    s += arr[i][N-1-i]