#크기가 N인 배열의 모든 원소레 접근하는 재귀함수
def f(i, N):
  if i == N:        #배열을 벗어남
      return
  else:             # 남은 원소가 있는 경우
    B[i] = A[i]
    f(i+1, N)

N = 3
A = [1,2,3]
B = [0] * N
f(0, N)