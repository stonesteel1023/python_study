# section 02 - 2
# import this
import sys

if sys.stdin == True:
    print(sys.stdin.encoding)
else:
    print("test " + sys.stdout.encoding)
    
# def hello():
#     print("Hello coding!")


# hello()

class Hellos:
    def hello(self):
        print("Hello coding!")

hi = Hellos()

hi.hello()