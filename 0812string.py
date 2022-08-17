# \o을 만나면 그 앞까지의 문자의 개수를 반환하는 함수
# def strlen(a):
#     count = 0
#     while 1:
#         if a[count] == '\0':
#             return count
#         count += 1
#
#
# print(strlen(['a','f','g','e','\0','a','f','w']))


# 문자열 뒤집기 연습
# str = list(input())
# result = [0] * len(str)
# for i in range(len(str)):
#     result[i] = str[len(str)-1-i]
#
# print(''.join(result))
#
# #교수님 풀이
# s= 'asdas asda'
# reverse_s = ''
#
# for i in range(len(s)-1, -1, -1):
#     reverse_s += s[i]
#
# print(reverse_s)

# list_s = list(input())
#
# for idx in range(len(list_s)//2):
#     list_s[idx], list_s[-idx-1] = list_s[-idx-1], list_s[idx]
# result = ''.join(list_s)
#
# print(result)

# s1 = 'abc'
# s2 = 'abc'
# s3 = 'def'
# s4 = s1
# s5 = s1[:2] + 'c'
#
# # == 비교
# print(s1 == s2) # T
# print(s1 == s3) # F
# print(s1 == s4) # T
# print(s1 == s5) # T
#
# # is 비교
# print(s1 is s2) # T
# print(s1 is s3) # F
# print(s1 is s4) # T
# print(s1 is s5) # F

# def my_strcmp(str1, str2):
#     n = min(len(str1), len(str2))
#     if str1 == str2:
#         return 0
#     else:
#         for i in range(n):
#             if ord(str1[i]) < ord(str2[i]):
#                 return -1
#             elif ord(str1[i]) == ord(str2[i]):
#                 pass
#             elif ord(str1[i]) > ord(str2[i]):
#                 return 1
#             elif i == len(str1)-1:
#                 return -1
# str1 = 'acc'
# str2 = 'abcd'
#
# for i in range(len)
#
# def llen(str):
#     count = 0
#     for i in range(len(str)):
#         count += 1
#     return count
#
# str1 = 'acc'
# str2 = 'abcd'
# if llen(str1) > llen(str2):
#     print(-1)
# elif llen(str1) == llen(str2):
#     print(0)
# else:
#     print(1)

# print(ord('2'))
# 문자 1 = 49
# 숫자 1과 48차이
#
# 정수 1을 입력 받으면
# 거기에 48을 더한후 chr()처리

# a = int(input())
# N = len(str(a))
# while a // 10 != 0:
#     b = a%10
#     a //= 10
#     print(chr(b+48), end='')
#
# def itoa(num):
#     if num == 0:
#         return '0'
#
#     # 음수, 양수의 경우 분리
#     if num < 0:
#         flag = False
#         num = -num
#     else:
#         flag = True
#
#     # 10으로 나눈 나머지를 하나하나 결과값에 더해줌
#     result = ''
#     while num:
#         num, remainder = num//10, num%10
#         result = chr(ord('0') + remainder) + result
#
#     # 음수인 경우 '-'붙여서 return
#     if flag:
#         return result
#     else:
#         return '-'+result


# brute force

def brute_force(pattern, target):
    N = len(target)
    M = len(pattern)

    i = 0 # target index
    j = 0 # pattern index

    while j < M and i < N:

        #틀렸을때
        if target[i] != pattern[j]:
            # 지금위치 -j + 1 하면 다음 위치가 됨
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    
    if j == M: # 검색 성공
        return i - M
    else:
        return -1 # 검색실패

target = 'This is a book~!'
pattern = 'is'
print(brute_force(pattern, target))

# KMP 알고리즘
    # lps(skip table)만드는 함수

def pre_process(P):
    lps = [0] * len(P)
    # lps를 만들기 위한 prefix의 인덱스
    j= 0

    for i in range(1, len(P)):
        #prefix의 idx 위치에 있는 char와 같으면 lps에 숫자 추가
        if P[i] == P[j]:
            lps[i] = j + 1
            j += 1
        else:
            j == 0
            if P[i] == P[j]:
                lps[i] = j + 1
                j += 1
    return lps

print(pre_process('abcdabcef'))
    
    # 실제 KMP 알고리즘
def KMP(T, P):
    lps = pre_process(P)

    # i : target을 순회하는 index
    # j : pattern을 순회하는 index
    i = 0
    j = 0

    position = -1

    while i < len(T):
        # 같으면 다음으로 이동
        if P[j] == T[i]:
            i += 1
            j += 1
        else:
            # 값은 다른데 j != 0라면, i자리는 유지, j만 이동해서 비교 시작
            if j != 0:
                j = lps[j - 1]
                print(f'j값 : {j}')
                print(f'lps[j-1 : {lps[j-1]}')
            #값은 다른데 j ==0 , i 값 한칸만 이동하고 처음부터 다시 진행
            else:
                i += 1
        if j == len(P):
            position = i - j
            break
    return position

T = 'abcdabeeababcdacef'
P = 'eaba'

position = KMP(T, P)

