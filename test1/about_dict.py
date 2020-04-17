# 자료구조 중 dictionary
## 1. 순서 없음
## 2. 중복 안됨
## 3. 수정 가능
## 4. 삭제 가능

# 선언 - key, value로 이루어짐
a = {1 : 'name', 2 : 'Phone', 3 : 'birth'}
aa = {'name' : 'Choi', 'Phone' : '010-7777-7777', 'birth' : 840920}
aaa = {'arr' : [1, 2, 3, 4, 5]}

##
print(1 in a)
print('name' not in a)

##
print(type(a), type(aa), type(aaa))
print(aa.get('name'), aa.get('address'))
print('함수1 keys = ',a.keys())
print('함수2 values = ',a.values())
print('함수3 item = ',aa.items())
print(aaa['arr'][0:3])

# dic 추가(순서 상관없음) - 그냥 집어넣으면 됨
aa['address'] = 'Gunposi'
print(aa)
aaa['rank'] = [6, 7, 8]
aaa['rank2'] = (0)
aaa['rank3'] = {9:0, 9:1, 9:2} # 중복 안되니까 맨 뒤에께 덮어씀
print(aaa) # 출력값 {'arr': [1, 2, 3, 4, 5], 'rank': [6, 7, 8], 'rank2': 0, 'rank3': {9}}

# 반복문 사용위한 dic 함수
temp = list(aa.keys())
print('함수1 keys = ',temp[0:3])
temp2 = list(aa.values())
print('함수2 values = ',temp2)
temp3 = list(aa.items())
print('함수3 items = ',temp3)

# for temp3 :
#     print(temp3)