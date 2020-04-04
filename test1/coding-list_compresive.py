# List Comprehension(리스트를 만드는 쉬운 방법들)
# append 시킬 변수 선언 x
# []에 한 줄로 조건절 넣기

numbers = []

# 일반적인 방법
# for n in range(1 ,101) :
#     numbers.append(n)
# print(numbers)

# 리스트 컴프리헨션
numbers2 = [x for x in range(1, 101)]
print(numbers2)

# 응용
# 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
# q3.remove(q3[3])
# for i in q3 :
#     print(i, end=' ')
# print()
print([x for x in q3 if x != "정"])


