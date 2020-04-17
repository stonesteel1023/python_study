# 문자열 (section04-2)

str1 = "I am a boy" #10
str2 = 'niceMan' #7
str3 = ""
str4 = str('')

# 문자열 함수
# 길이구하기
print(len(str1), len(str2), len(str3), len(str4))
# 뭐지? -> boolean
print(str1.islower())
# y로 끝나는지 boolean
print(str1.endswith('y'))
# 맨 처음글자 대문자
print(str2.capitalize())
# 문자 교체
print(str1.replace('boy', 'girl'))
# 역순으로 리스트에 넣어서 
print(list(reversed(str1)))
# 짤라서 출력
print(str1[0:4])
print(str1[0:len(str1)-2])
print(str1[:])
print(str1[0:7:3]) # indexing을 가지고 짜름
print(str1[1:-2]) # 1부터 맨뒤(len)에서 -2까지
print(str1[::-1]) # 처음부터 끝까지, 역순으로 

# escape
escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String
raw_str1 = r'C:\Coding\python_work\test1'
raw_str2 = r"\\a\\a"
print(raw_str1)
print(raw_str2)

# Multi Line
multi = \
"""
문자열
멀티라인
테스트
"""
print(multi)

# String calc
o1 = '*'
o2 = 'abc'
o3 = "def"
o4 = "Niceman"

print(o1 * 10)
print(o2 + o3)
print(o1 + '3')
print(o1 * int('3'))
print('n' in o4, 'N' in o4, 'E' not in o4, 'e' in o4)