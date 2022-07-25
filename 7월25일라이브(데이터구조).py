'''print('apple'.find('p')) # 1
print('apple'.find('k')) # -1
#print('apple'.index('k')) # 오류출력
print('abc'.isalpha()) # True
print('ㄱㄴㄷ'.isalpha()) # True
print('Ab'.isupper()) # False

print('a,b,c'.split(','))
print('a,b,c'.split())
print('서울시 강남구 삼성동'.split()[0])

msg = 'hI! Everyone, I\'m ssafy'

print(msg) # hI! Everyone, I'm ssafy
print(msg.capitalize()) # Hi! everyone, i'm ssafy
print(msg.title()) # Hi! Everyone, I'M Ssafy
print(msg.upper()) # HI! EVERYONE, I'M SSAFY
print(msg.lower()) # hi! everyone, i'm ssafy
print(msg.swapcase()) # Hi! eVERYONE, i'M SSAFY

print('*'.join('ssafy')) # s*s*a*f*y
print(' '.join(['3', '5'])) # 3 5

cafe =['starbucks', 'tomntoms']
print(cafe)
cafe.append('banapresso')
print(cafe)
cafe.insert(1, 'start')
print(cafe)
cafe.insert(1000, 'end')
print(cafe)
cafe.extend(['coffee'])
print(cafe)
cafe.extend('cup')
print(cafe)

numbers = [1, 2, 3, 'hi']
print(numbers)
numbers.remove('hi')
print(numbers)
numbers.remove('hii')
print(numbers)'''

"""numbers = [1, 2, 3, 'hi']
print(numbers)
word = numbers.pop()
print(word)
print(numbers)
numbers.clear()
print(numbers)

numbers = [1, 2, 3, 1, 1]
print(numbers.count(1))
print(numbers.count(100))


numbers = [3, 2, 5, 7]
result = numbers.sort()
print(numbers, result) # result에 값이 반환되지 않아서 none 반환


numbers = [3, 2, 6, 8]
# result = numbers.sorted() # 오류
result = sorted(numbers)
print(numbers, result)

numbers = [3, 2, 5, 1]
result = numbers.reverse()
print(numbers, result)

a = (1, 2, 3, 5, 1)
#a[0] = 5 # 오류. 튜블은 immutable

day_name = ('월', '화', '수', '목', '금') 
print(type(day_name))

print(day_name[-3])
print(day_name * 2)
print(id(day_name))
day_name += False, True
print(day_name)"""

"""print('apple' in 'a') # False
print('a' in 'apple') # True
print('hi' in 'hi I am ssafy') # True
print('서순' in ['서순', '요까일엇무', '기러기']) # True
print('서순' in ['요까일엇무', '기러기']) # False"""

"""a = {'사과', '바나나', '수박'}
print(type(a))
print(a)
print(a.add('딸기'))
print(a)
a.update(['딸기', '바나나', '참외'])
print(a)
a.remove('딸기')
print(a)
#a.remove('딸기')
#print(a) # 없는값 지우면 에러
a.discard('딸기')
print(a) # discard는 없는값 버려도 오류 안남"""

"""a = {'사과', '바나나', '수박'}
a.clear()
print(a)

a = {'사과', '바나나', '수박'}
b = {'포도', '망고'}
c = {'사과', '포도', '망고', '수박', '바나나'}
print(a.isdisjoint(b)) # True
print(a.isdisjoint(c)) # False
print(a.issubset(c)) # True
print(b.issubset(c)) # True
print(a.issuperset(c)) # False
print(c.issuperset(a)) # True"""

"""my_dict = {'apple' : '사', 'banana' : '바나나'}
my_dict.update(apple='사과')
print(my_dict)"""

"""my_dict = {'apple' : '사과', 'banana' : '바나나'}

for value in my_dict.values():
    print(value)
    
for key, value in my_dict.items():
    print(f'key: {key} / value: {value}')"""
    
"""original_list = [1, 2, 3]
#copy_list = original_list
copy_list = original_list[:]
print(original_list, copy_list)

copy_list[0] = 'hello'
print(original_list, copy_list)"""
    
"""a ={1, 2, 3}
b = a[:]
b[0] = 5
print(a, b)"""

import copy

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = copy.deepcopy(a)
print(a, b)
b[0][2] = 'hello'
print(a, b)