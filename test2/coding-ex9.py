# hint

def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return (y1, y2, y3)

val = func_mul(1)
print(type(val), val)

# 비교
def func_mul2(x : int):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return (y1, y2, y3)

val2 = func_mul2(1.0)
print(type(val2), val2)
    
# 람다식 - (익명함수 사용으로)간결한 코드, 메모리 절약, 가독성 향상 
# BUT 오히려 헷갈림, 그리고 메모리가 엄청 절약되는 것도 아님
# 람다는 즉시 실행(힙 메모리에서 실행됨)

def mul_10(num : int) -> int:
    return num * 10

func_var = mul_10
print(type(func_var), mul_10(1))
print(func_var(1))

# 비교
lambda_mul_10 = lambda num : num * 10
print(lambda_mul_10(1))

## 매개변수로 함수 만들어서 넘기기
def func_lambda(x, y, func):
    print(x * y * func(1))
    
func_lambda(1, 1, lambda_mul_10)

## 매개변수로 넘기면서 함수 생성하기
print(func_lambda(1, 1, lambda num : num * 10))
