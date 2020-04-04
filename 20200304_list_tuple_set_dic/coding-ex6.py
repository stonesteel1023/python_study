# 자료형1 - 리스트, 튜플

# name1 = 'Lee';
# print(name1);

# list 
## 1. 순서 있음
## 2. 중복 가능
## 3. 수정 가능
## 4. 삭제 가능

# 리스트 선언
a = []
b = list()
# print(type(a), type(b))
c = [1, 2, 3, 4]
d = [10, 100, 'Apple', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Eraser', 'Ruler']]

# indexing
print(d[3], d[-2])
print(e[2][0], e[-1][-3])

# slicing
print(d[0:2])
print(e[2])
print(e[2][0:3])

# 리스트 결합
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)
c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a', 'b', 'c']
print(c)
del c[1]
print(c)
del c[-1]
print(c)

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.reverse();
print(y)
y.sort();
print(y)
print(y[0], y[-1])
y.reverse();
print(y)
# 2번째에 7을 삽입
y.insert(2, 7)
print(y)
# 리스트 안에서 2를 지움
y.remove(2)
print(y)
# pop - stack에서 맨 마지막의 숫자를 꺼내버림(지움)
y.pop()
print(y)
#y.push(0) - 존재하지 않음
#print(y)
# 리스트 마지막에 추가
y.append(0)
print(y)
# 리스트 마지막에 연장하는 함수
ex = [0, 0]
y.extend(ex)
print(y)