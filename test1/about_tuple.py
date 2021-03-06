# 자료형2 - 리스트, 튜플

# tuple
## 1. 순서 있음
## 2. 중복 가능
## 3. 수정 안됨 - 변경안되야하는 값에 적용 - 함수 적음
## 4. 삭제 안됨 - 예) 통장잔고 저장 자료구조

# 배열 선언 ()로 묶음

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

# del c

print(c[0])
print(d[2][1])

# indexing & slicing

print(d[2:])
print(d[2][0:2])

# 확장

print(c + d)
print(c * 3)
# 자료형1 - 리스트, 튜플

# name1 = 'Lee';
# print(name1);

# list 
## 1. 순서 있음
## 2. 중복 가능
## 3. 수정 가능
## 4. 삭제 가능

# 리스트 선언
# 함수

z = (5, 2, 1, 3, 4)

# 3이 있는지 확인(true/false), 
# 3이 몇개 들어있는지 세기(int 반환)
# 3번째 index 값 꺼내기
print(z, 3 in z, z.count(1), z.index(3))

