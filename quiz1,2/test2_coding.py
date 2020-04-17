# flow control(if/for) test 16Q

# 1 ~ 5 문제 if 조건문 사용
# 6 ~ 10 문제 while 또는 for 반복문 사용

# Q1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
# print(list(q1.keys())[2])
if list(q1.keys())[2] == '가을':
    print(q1.get(list(q1.keys())[2]))

# Q2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
if tuple(q2.values()).count('사과') >= 1:
    print('포함됨')
else :
    print('없음')

# Q3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A, 61 ~ 80 :  B, 41 ~ 60 :  C, 21 ~ 40 :  D, 0 ~ 20 :  E (학점)
score = 20
if 81 <= score <= 100 :
    print('A')
elif 61 <= score <= 80 :
    print('B')
elif 41 <= score <= 60 :
    print('C')
elif 21 <= score <= 40 :
    print('D')
else :
    print('E')

# Q4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.
# 12, 6, 18
int1, int2, int3 = 12, 6, 18
# print(max(12, 6, 18))
# list_int = [12, 6, 18]
# maxValue = list_int[0]
# for i in range(1, len(list_int)):
#     if maxValue < list_int[i]:
#         maxValue = list_int[i]
# print(maxValue)
if (int1 > int2) & (int1 > int3) :
    print(int1)
elif (int2 > int1) & (int2 > int3) :
    print(int2)
elif (int3 > int1) & (int3 > int2) :
    print(int3)

# Q5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. 
# (1,3 : 남자, 2,4 : 여자)

int5 = 3062229
list_int5 = list(str(int5))
if list_int5[0] == '1' or list_int5[0] == '3' :
    print('남자')
elif list_int5[0] == '2' or  list_int5[0] == '4' :
    print('여자')
    
# Q6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
q3.remove(q3[3])
# print(type(q3), type(q3.pop("정")))
for i in q3 :
    print(i, end=' ')
print()
# for v in q3 :
#     if v == "정" :
#         continue
#     print(v)

# Q7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
i2 = 1
while i2 <= 100 :
    print(i2, end=' ')
    i2 = i2 + 2
print()
# for v2 in range(1, 100) :
#     if v2 % 2 != 0 :
#         print(v2, end=' ')

# Q8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for str8 in q4 :
    if len(str8) >= 5 :
        print(str8, end=' ')
print()

# Q9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for str9 in q5 :
    if str9.islower() :
        print(str9, end=' ')
print()

# Q10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for str10 in q6 :
    if str10.islower() :
        print(str10.upper(), end=' ')
    elif str10.isupper() :
        print(str10.lower(), end=' ')
print()
