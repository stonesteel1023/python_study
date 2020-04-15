# python_study
2월28일부터 4개월동안 파이썬 스터디 내용 업로드

## 20200303_list_tuple 
- 파이썬 자료구조 중 리스트, 튜플에 대한 스터디 : coding-ex6.py, coding-ex7.py

## 20200304_list_tuple_set_dic
- 파이썬 자료구조 중 디셔너리, 집합에 대한 스터디 : coding-dic.py, coding-ex8.py

## pyDB
- SQLlite 이용해서 파이썬 게임 만들기

## fastgram
- 파이썬으로 패스트(캠프)인스타그램 만들기

### data type test 16문, flow control(if/for) test 16문
- test_coding.py
- test2_coding.py


## [Python 변수] mutable과 immutable의 차이

<p style="text-align: left;"><span style="font-size: 18.6666660308838px; line-height: 28px;"><b><u>변수</u></b></span></p><p style="text-align: left;"><span style="font-size: 18.6666660308838px; line-height: 28px;"><span style="font-size: 12pt;"><u style="font-weight: bold;"></u>변수는 객체를 가리킨다.</span><br /></span></p><p style="text-align: left;"><span style="font-size: 16px; line-height: 24px;">$$ num = 10 $$</span></p><p style="text-align: left;"><span style="font-size: 16px; line-height: 24px;">컴퓨터 메모리에 10이라는 값이 저장되고 num은 10이 저장된 메모리의 위치를 가리킨다.</span></p><p style="text-align: left;"><span style="font-size: 16px; line-height: 24px;">10이라는 정수형 객체를 num이라는 변수가 가리키고 있는 것이다.</span></p><p style="text-align: left;"><span style="font-size: 16px; line-height: 24px;"><br /></span></p><p style="text-align: left;"><span style="font-size: 18.6666660308838px; line-height: 28px;"><b><u>mutable, immutable</u></b></span></p><p style="text-align: left;"><span style="font-size: 12pt;">mutable은 값이 변한다는 뜻이고, immutable은 값이 변하지 않는다는 의미이다. 자료형마다 특징이 다른데 코드를 통해 알아보도록 하자.</span><br /></p><p style="text-align: left;"><span style="font-size: 12pt;"><b>- 숫자형 (Number) : immutable</b></span></p><p style="text-align: center; clear: none; float: none;"><span class="imageblock" style="display:inline-block;width:300px;;height:auto;max-width:100%"><img srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile10.uf.tistory.com%2Fimage%2F276C134655A74C8E09424E" src="https://t1.daumcdn.net/cfile/tistory/276C134655A74C8E09" style="max-width:100%;height:auto" width="300" height="248" filename="python_immutable.png" filemime="image/jpeg" style=""""/></span></p><p style="text-align: center; clear: none; float: none;"><br /></p><p style="text-align: left; clear: none; float: none;"><b style="font-size: 16px; line-height: 24px; text-align: left;">- 문자열 (String) : immutable</b></p><p style="text-align: center; clear: none; float: none;"><span class="imageblock" style="display:inline-block;width:300px;;height:auto;max-width:100%"><img srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile10.uf.tistory.com%2Fimage%2F2177D13B55A74D97322487" src="https://t1.daumcdn.net/cfile/tistory/2177D13B55A74D9732" style="max-width:100%;height:auto" width="300" height="248" filename="python_immutable_string.png" filemime="image/jpeg" style=""""/></span></p><p style="text-align: center; clear: none; float: none;"><br /></p><p style="text-align: left;"><span style="font-size: 12pt;"><b></b></span><b style="font-size: 16px; line-height: 24px;">- 리스트&nbsp;(List) : mutable</b></p><p style="text-align: center; clear: none; float: none;"><span class="imageblock" style="display:inline-block;width:300px;;height:auto;max-width:100%"><img srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile4.uf.tistory.com%2Fimage%2F244AB53955A74E552B27F4" src="https://t1.daumcdn.net/cfile/tistory/244AB53955A74E552B" style="max-width:100%;height:auto" width="300" height="248" filename="python_mutable_list.png" filemime="image/jpeg" style=""""/></span></p><p style="text-align: center; clear: none; float: none;"><br /></p><p style="text-align: left; clear: none; float: none;"><b style="text-align: left; font-size: 16px; line-height: 24px;">- 튜플&nbsp;(Tuple) : immutable</b></p><p style="text-align: center; clear: none; float: none;"><span class="imageblock" style="display:inline-block;width:300px;;height:auto;max-width:100%"><img srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile2.uf.tistory.com%2Fimage%2F2664A14255A74F0E296014" src="https://t1.daumcdn.net/cfile/tistory/2664A14255A74F0E29" style="max-width:100%;height:auto" width="300" height="248" filename="python_immutable_tuple.png" filemime="image/jpeg" style=""""/></span></p><p style="text-align: center; clear: none; float: none;"><br /></p><p style="text-align: left; clear: none; float: none;"><b style="text-align: left; font-size: 16px; line-height: 24px;">- 딕셔너리&nbsp;(Dictionary) : mutable</b></p><p style="text-align: center; clear: none; float: none;"><span class="imageblock" style="display:inline-block;width:300px;;height:auto;max-width:100%"><img srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile10.uf.tistory.com%2Fimage%2F23722E4655A7504C1405B3" src="https://t1.daumcdn.net/cfile/tistory/23722E4655A7504C14" style="max-width:100%;height:auto" width="300" height="248" filename="python_mutable_dictionary.png" filemime="image/jpeg" style=""""/></span></p><p style="text-align: center; clear: none; float: none;"><br /></p><p style="text-align: left; clear: none; float: none;"><span style="font-size: 12pt;">숫자, 문자열, 튜플은 변경이 불가능하고 리스트와 딕셔너리는 변경이 가능하다. 위 코드의 $y=x$부분에서 y와 x가 같은 주소 값을 가리키게 되는데, 리스트의 [:]나 deepcopy 함수를 이용하면 같은 객체를 공유하지 않도록 사용 가능하다.</span></p>
  
```
# copy 모듈 import
import copy
 
x = [1,2]
# x 변수가 저장하고 있는 주소 값 대입
y = x
# x와 z가 같은 객체를 공유하지 않는다.(리스트만 가능)
z = x[:]
# deepcopy를 이용하면 x와 cpy가 같은 객체를 공유하지 않는다.
dcpy = copy.deepcopy(x)
 
print id(x)
print id(y)
print id(z)
print id(dcpy)
```
```
35300696
35300696
35299496
35302536
```
<p style="text-align: left; clear: none; float: none;"><span style="font-size: 18.6666660308838px; line-height: 28px;"><b><u>정리</u></b></span></p><p style="text-align: left; clear: none; float: none;"><span style="font-size: 12pt; line-height: 28px;">immutable, mutable 속성은 매우 중요하다. 이 속성에 따라 변수가 함수의 매개변수로 전달될 때 원래 입력 변수값이 변경되는지 안되는지 결정된다. Call-By-Value, Call-By-Reference와 동일한 개념이다. 이해가 되지 않으면 직접 코딩해보고 차이점을 인지해야 한다.</span></p><p style="text-align: left;"><br /></p>

## 파이썬 함수 오버로딩

### 1.편집 Python 3.4의 새로운 단일 디스패치 제네릭 함수에 대해서는 http://www.python.org/dev/peps/pep-0443/을 참조하십시오.
편집 Python 3.4의 새로운 단일 디스패치 제네릭 함수에 대해서는 http://www.python.org/dev/peps/pep-0443/을 참조하십시오.

일반적으로 Python에서 함수를 오버로드 할 필요는 없습니다. 파이썬은 동적으로 타입이 지정되며 함수에 대한 선택적 인수를 지원합니다.
```
def myfunction(first, second, third = None):
    if third is None:
        #just use first and second
    else:
        #use all three

myfunction(1, 2) # third will be None, so enter the 'if' clause
myfunction(3, 4, 5) # third isn't None, it's 5, so enter the 'else' clause
```
==============================
### 2.보통 파이썬에서는 원하는 것을 할 수 없습니다. 두 가지 근사치가 있습니다.
보통 파이썬에서는 원하는 것을 할 수 없습니다. 두 가지 근사치가 있습니다.
```
def myfunction(first, second, *args):
    # args is a tuple of extra arguments

def myfunction(first, second, third=None):
    # third is optional
```
