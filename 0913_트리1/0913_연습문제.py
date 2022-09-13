'''
첫줄에는 트리의 정점의 총 수 V가 주어진다. 그 다음 줄에는 V-1개 간선이 나열된다.
간선은 그것을 이루는 두 정점으로 표기된다. 간선은 항상 "부모 자식"순서로 표기된다.
아래 예에서 두 번째 줄 처음 1과 2는 정점 1과 2를 잇는 간선을 의미하며 1이 부모, 2가 자식을 의미한다.
간선은 부모 정점 번호가 작은 것부터 나열되고, 부모 정점이 동일하다면 자식 정점 번호가 작은 것부터 나열된다

다음 이진 트리 표현에 대하여 전위 순회하여 정점의 번호를 출력하시오
V : 13 정점의 개수
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def find_root(par):                 # root찾기
    for i in range(1, V+1):
        if par[i] == 0:
            return i
        
def pre(n):                         # 전위 순회
    # global cnt
    if n:
        print(n, end=' ')
        # cnt += 1
        pre(ch1[n])
        pre(ch2[n])

def inorder(n):                     # 중위순회
    if n:
        inorder(ch1[n])
        print(n, end=' ')
        inorder(ch2[n])
        
def postorder(n):                   # 후위 순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end=' ')
        
V = int(input())                    # 정점 수
E = V - 1                           # 간선 수
arr = list(map(int, input().split()))   # 간선 표현 list
ch1 = [0]*(V+1)                     # 왼쪽 자식
ch2 = [0]*(V+1)                     # 오른쪽 자식
par = [0]*(V+1)                     # 자식 기준 부모

for i in range(0, 2*E, 2):
    if ch1[arr[i]] == 0:
        ch1[arr[i]] = arr[i+1]
    else:
        ch2[arr[i]] = arr[i+1]
    par[arr[i+1]] = arr[i]
    
n = find_root(par)
cnt = 0
pre(n)
print(cnt)
inorder(n)
print()
postorder(n)