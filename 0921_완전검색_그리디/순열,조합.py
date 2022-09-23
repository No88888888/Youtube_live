N, M = map(int, input().split()) # 4 2 
#  1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
def nPm():
    if len(s) == M:
        print(*s)
        return
    for i in arr: # 1 2 3 4 5
        if i in s:
            continue
        else:
            s.append(i)  # 1  
            nPm()
            s.pop()

arr = [i for i in range(1, N+1)]
# combi = []
s = [] # 임시로 지금 순열 
nPm()





N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
combination_ = []
s = []

def nCm():
    if len(s) == M:
        t = s[:]
        s.sort()
        if t in combination_:
            pass
        else:
            combination_.append(t)
            print(*t)
        return

    for i in arr:
        if i in s:
            continue
        else:
            s.append(i)
            nCm()
            s.pop()

nCm()