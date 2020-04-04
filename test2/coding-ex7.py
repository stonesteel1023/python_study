# 리턴값 존재
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return('python777')
print(str)

# 다중 리턴
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(1)
print(val1, val2, val3)
    