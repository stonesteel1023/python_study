# data type test 16Q

# Q1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(str.__len__(q1))

# Q2. 출력   apple;orange;banana;lemon
# print('apple;orange;banana;lemon')
print('apple','orange','banana','lemon',sep=';')

# Q3. 화면에 * 기호 100개를 표시하세요.
print('*' * 100)

# Q4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
str1 = '30'
print(int(str1), float(str1), complex(str1), chr(51)+''+chr(48))
# print(float(str1))
# print(complex(str1))
# print(chr(51)+''+chr(48))

# Q5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
str2 = "Niceman"
# print(str2.split("Nice",-1)[1]) 
print(str2[str2.index('m'):str2.index('n')+1])

# Q6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
str3 = "Strawberry"
rev_list3 = str3[::-1]
print(rev_list3)
# list3 = list("Strawberry")
# print(type(list3), list3)
# list3.reverse()
# for li in list3 :
#     print(li, end='')
# print()

# Q7. 문자열 "010-7777-9999"에서 '-'를 제거 후 출력하세요.
str7 = "010-7777-9999"
# print(str7[0:3]+str7[4:8]+str7[9:13])
# str3 = str7.split('-', -1)
# print(str3[0]+''+str3[1]+''+str3[2])
import re # regular express
print(re.sub('[^0-9]','',str7))

# Q8. 문자열 "http://daum.net"에서 "http://" 부분을 제거 후 출력하세요.
str8 = "http://daum.net"
# str4 = str8.split('http://', -1)
# print(str4[1])
print(str8[7:])

# Q9. 문자열 "NiceMan"을 모두 대문자, 소문자로 각각 출력해보세요.
str9 = "NiceMan"
small_str9 = str9.lower()
big_str9 = str9.upper()
print(big_str9, small_str9)

# Q10. 문자열 "abcdefghijklmn"을 슬라이싱을 이용해서 "cde"만 출력하세요.
str10 = "abcdefghijklmn"
print(str10[2:5])
# arr_str10 = ("abcdefghijklmn")
# print(arr_str10[2:5])

# Q11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
list11 = ["Banana", "Apple", "Orange"]
list11.remove(list11[1])
print(list11)

# Q12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
t12 = (1, 2, 3, 4)
l12 = list(t12)
print(type(l12), l12)

# Q13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : 
# <성인 - 100000 , 
# 청소년 - 70000 , 
# 아동 - 30000>
dic1 = {}
dic1['성인'] = 100000
dic1['청소년'] = 70000
dic1['아동'] = 30000
print(dic1)

# Q14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
dic1['소아'] = 0
print(dic1)

# Q15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
list15 = list(dic1.keys())
# print(list15)
for li2 in list15 :
    print(li2, end=' ')
print()

# Q16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
list16 = list(dic1.values())
# print(list16)
for li3 in list16 :
    print(li3, end=' ')
print()