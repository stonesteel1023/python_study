class Fibonacci:
    def __init__(self, title = "fibonacci"):
        self.title = title
        
    def fib(num : int):
        a, b = 0, 1
        while a < num:
            print(a, end=' ')
            a, b = b, a+b
        print()
        
    def fib2(num : int):
        result = []
        a, b = 0, 1
        while a < num:
            result.append(a)
            a, b = b, a+b
        return result

# Fibonacci.fib(3)
# Fibonacci.fib2(3)

# unit test
if __name__ == "__main__":
    Fibonacci.fib(3)
    print(Fibonacci.fib2(3))
