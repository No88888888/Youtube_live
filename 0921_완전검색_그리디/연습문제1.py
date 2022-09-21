def select(A, s):
    n = len(A)
    if s == n-1:
        return
    minV = s
    for i in range(s, n):
        if A[minV] > A[i]:
            minV = i
    A[s], A[minV] = A[minV], A[s]
    select(A,s+1)




A = [2,4,6,1,9,8,7,0]
select(A,0)
print(A)