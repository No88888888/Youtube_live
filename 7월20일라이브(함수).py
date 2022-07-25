"""from re import A


fruits = ['apple', 'mango', 'banana']
for fruit in fruits:
    print(fruit)
print('끝')


#LEGB 예시
# 아래코드 실행결과는?

a = 0
b = 1
def enclosed():
    a = 10
    c = 3
    def local(c):
        print(a, b, c)
    local(300)
    print(a, b, c)
enclosed()
print(a, b)

#global예시

a = 10
def func1():
    global a
    a = 3

print(a)
func1()
print(a)"""

#for문을 이용한 문자열 순회

"""chars = input()

for idx in range(len(chars)):
    print(chars[idx])"""

#딕셔너리 순회

"""grades = {'john' : 80, 'eric' : 90}
print(grades.keys())
print(grades.values())
print(grades.items())

for student, grade in grades.items():
    print(student, grade)"""
    
#enumerate 순회

"""members = ['민수', '영희', '철수']

for idx, number in enumerate(members):
    print(idx, number)"""
    
#list comprehension

cubic_list = []
for number in range(1, 4):
    cubic_list.append(number**3)
print(cubic_list)

#dictionary comprehention

cubic_dict = {}

for number in range(1, 4):
    cubic_dict[number] = number**3
print(cubic_dict)