# 함수호출

# 함수명(parameter) <- 함수 선언하는 위치 중요

## 리턴값 없음
def hello(world):
    print("Hello", world)
    
hello('python')
hello(777)

## 리턴값 존재
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return('python777')
print(str)

## 다중 리턴 -> 리스트로 리턴
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

list_val = func_mul(1)
print(list_val, type(list_val))

## 인자 받기 *args
def args_func(*args):
    print(type(args))
    for i, t in enumerate(args):
        print(i, t)
    
args_func("Kim", "Lee", "Park")

## 인자 받기 **kwargs
def kwargs_func(**kwargs):
    print(type(kwargs))
    for k, t in kwargs.items():
        print(k, t)

kwargs_func(name1 = "kim", name2 = "lee", name3 = "park")

### 결론(전체 합치기)

def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)
    
example_mul(10, 20, 'park', 'kim', age1 = 24, age2 = 35)

