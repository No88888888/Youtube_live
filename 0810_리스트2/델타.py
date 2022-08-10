# 2차배열의 한 좌표에서 4방향의 인접 요소를 탐색하는 방법
N = int(input())
M = int(input())
di = []
dj = []
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[i]
            nj = j + dj[j]
            if 0<=ni<N and 0<=nj<M:
                print(ni, nj)

for i in range(N):
    for j in range(M):
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + dj, j + dj
            if 0<=ni<N and 0<=nj<M:
                print(ni, nj) 

#인접 2개씩의 요소 탐색 방법(위 두개 아래 두개 등)

di = []
dj = []
for i in range(N):
	for j in range(N):
		for k in range(4):
			for d in range(1, 3):
				ni = i + di[i] * d
				nj = j + dj[j] * d
				if 0<=ni<N and 0<=nj<M:
					print(ni, nj)