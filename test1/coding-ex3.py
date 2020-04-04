str_var = "Nice Man"
str_var2 = "Good Boy"
bool_var = True 
float_var = 10.3
int_var = 7
dic_var = {"name" : "Choi",
           "age" : 25
           }
list_var = [3, 5, 7]
tup_var = 3, 5, 7
set_var = {7, 8, 9}

#자료형 프린트해보기
print(type(tup_var))
print(type(set_var))
print(type(list_var))
print(type(dic_var))
print(type(int_var))
print(type(float_var))
print(type(bool_var))
print(type(str_var2),str_var2)
print(type(str_var),str_var)

int1 = 39
int2 = 939
big_int3 = 999999999999999999999999999999999999999
big_f1 = 777777777777777777777777777777777777777
f2 = 1.234
f3 = 3.784
f4 = .5
f5 = 10.

print(int1 * int2)
print(big_f1 * big_int3)
print(f2 ** f3)
# 자동 형변환
print(f4 + int2)
# 증명
result = f4 + int2
print(result, type(result))

# 수동 형변환
a = 5.
b = 4
print(type(a), type(b))
result2 = a + b
print(result2, type(result2))
# 실행
print(int(result2), type(int(result2)))

# 형변환
print(3)
print(int('3'))
print(chr(51))

# 문자열 형변환
print(str(65), type(str(65)), str(65) + chr(65))
print(str(10.4))