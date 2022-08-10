# N = 3 # 행
# M = 4 # 얄
# # N개의 원소를 갖는 0으로 초기화된 1차원배열
# arr1 = [0]*N
#
# # 크기가 NxM이고 0으로 초기화된 2차원 배열
# arr2 = [[0]*M for _ in range(N)]
# print(arr2)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0
for i in range(N):
    for j in range(N):
        s += arr[i][j]
print(s)

