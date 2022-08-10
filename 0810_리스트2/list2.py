# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# #
# # print(arr)

# for i in range(N):
#     for j in range(N):
#         print(arr[i][j], end=' ')
#     print()

# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# N = 3
# M = 4
# arr = [[1,2,3,4], [4,5,6,8]]
# for i in range(N):
#     for j in range(M):
#         for d in range(1,3):
#             for k in range(4):
#                 ni = i + dj[k] * d
#                 nj = j + dj[k] * d
#                 if 0<=ni<N and 0<=nj<M:
#                     print(ni, nj)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 3
M = 4

for i in range(N):
    for j in range(M):
        for k in range(4):
            ni = i + dj[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M:
                print(ni, nj)

# arr = [7,2,5,3,4,6]
# N = len(arr)

# def up(arr, N):
#     for i in range(N):
#         minidx = i
#         for j in range(i+1, N):
#             if arr[j] < arr[minidx]:
#                 minidx = j
#         arr[minidx], arr[j] = arr[j], arr[minidx]
#         return arr

# print(up(arr, 6))

