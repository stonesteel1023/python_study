# 자료형3 - 집합

# set
## 1. 순서 없음
## 2. 중복 허용 안됨

b = set()
bb = set([1, 2, 3, 4])
bbb = set([1, 4, 5, 6, 6]) # 중복안됨

##
print(type(b), type(bb), type(bbb))
print(b, bb, bbb)

t = tuple(bb)
print(type(t), t)
l = list(bb)
print(type(l), l)

##
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

## 교집합
print(s1.intersection(s2))
print(s2 & s1)

## 합집합
print(s1.union(s2))
print(s2 | s1)

## 차집합
print(s1.difference(s2))
print(s1 - s2)

# 집합 추가 & 삭제
s3 = set([7, 8, 10, 15])
s3.add(18)
s3.add(7) # 중복안됨 - 에러는 안남
print(s3)
s3.remove(15)
print(s3)
s3.clear()
print(type(s3), s3)