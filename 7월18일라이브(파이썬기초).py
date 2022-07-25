print(not True) # False
print(not 0) # True
print(not 'hi') # False
print(not True and False or not False) # True
# 위와 같음
print(((not True) and False) or (not False)) # True

# 논리 연산자 우선순위 존재
# not, and, or순으로 우선순위 높음

#논리 연산자의 단축평가
"""
결과가 확실한 경우 구번째 값은 확인하지 않고 첫번째 값 반환
and 연산에서 첫번째 값이 True인 경우  무조건 False =>첫번째 값 반환
or 연산에서 첫번째 값이 True인 경우 무조건 True => 첫번째 값 반환
0은 False, 1은 True
"""

print(3 and 5) # 5
print(3 and 0) # 0
print(0 and 3) # 0
print(0 and 3) # 0
print(0 and 0) # 0

print(5 or 3) # 5
print(3 or 0) # 3
print(0 or 3) # 3
print(0 or 0) # 0

a = 5 and 4
print(a) # 4

b = 5 or 3
print(b) # 5

c = 0 and 5
print(c) # 0

d = 5 or 0
print(d) # 5

