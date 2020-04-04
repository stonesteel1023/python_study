# 클로져(함수 안에 함수가 존재) -> 데코레이터

def nested_func(num):
    print("in nested func1")
    #func_in_func(num + 1000)
    def func_in_func(num):
        print("in func3")
        print(num)
    print("in nested func2")
    func_in_func(num + 1000)

nested_func(1000)
# 결과값
# in nested func1
# in nested func2
# in func3
# 2000

