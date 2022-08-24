from collections import deque
p = 1           # 처음 줄 설 사함 번호
q = []
# q =deque()
N = 20    # 초기 마이쮸 갯수
m = 0           # 나눠준 갯수
v = 0

while m < N:
    # input()
    q.append((p,1,0))   # 처음 줄 서는 사람
    # print(q)
    v,c,my = q.pop(0)
    print(f'큐에 있는 사람 수 {len(q)+1}, 받아갈 사탕 수{c}, 나눠준 사탕 수{m}')
    m += c
    q.append((v, c+1, my+c))    # 마이쮸를 받고 다시 줄 서는 사람
    p += 1
print(f'마지막 받은 사람:{v}')


#===================================

# queue = []

# my_chu = 20

# next_person = 1
# # 1번이 줄선다
# queue.append([1, 1])

# while 1:
#     # n번이 마이쮸 1개를 가져간다
#     idx, num = queue.pop(0)
#     my_chu -= num
#     # n번이 다시 줄을 선다
#     queue.append([idx, num + 1])
#     next_person += 1
#     # 새로운 사람이 줄을 선다
#     queue.append([next_person, 1])
#     #print(queue)
    
#     input()
#     print(f'줄에 서있는 사람: {len(queue)}')
#     print(f'현재 1인당 나눠주는 마이쮸: {num}')
#     print(f'현재까지 나눠준 사탕: {20 - my_chu}')
    
#     if my_chu <= 0:
#         break