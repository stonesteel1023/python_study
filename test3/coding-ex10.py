
# 기본 패키지 불러오기 방법
from package.fibonachi import Fibonacci

Fibonacci.fib(15)

print("list_fibonacci : ", Fibonacci.fib2(15))

print("Title :", Fibonacci().title)

# 그냥 전부 패키지 불러오기 방법(메모리 많이 먹을 가능성)
from package.fibonachi import *

print("list_fibonacci : ", Fibonacci.fib2(60))

print("Title :", Fibonacci().title)

# alias로써 패키지 불러오기 방법
from package.fibonachi import Fibonacci as fb

fb.fib(1000)

print("list_fibonacci : ", fb.fib2(1000))

print("Title :", fb().title)


# 기본 패키지 불러오기 방법(alias는 cal)
import package.calculations as cal

print("calculate", cal.add(10, 100))
print("calculate", cal.minus(10, 100))
print("calculate", cal.mul(10, 100))


# 패키지 안에서 필요한 함수만 불러오기 방법(alias는 d)
from package.calculations import div as d
print("calculate", d(10, 100))

# # 기본 패키지 불러오기 방법(alias는 cal)
import package.print_lib as p
import builtins
p.print_boy()
p.print_girl()
print(dir(builtins))