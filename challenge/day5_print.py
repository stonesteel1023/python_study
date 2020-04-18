import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"

# post_data = {'format':'json', 'api_key':'[YOUR_API_KEY]','iban':'DE46500700100927353010'}
# response = requests.post('https://api.iban.com/clients/api/v4/iban/',post_data)
# print(response.text)

# 기본 파싱
iban_result = requests.get(url)
iban_soup = BeautifulSoup(iban_result.text, "html.parser")

# class는 못찾았고 table 밑에 tr 안에 td 다 검색해오기
trtd = iban_soup.select("tr td")

# 일단 텍스트로 뽑아서 다 넣어버리기
lists_td = []
for c in trtd :
  lists_td.append(c.get_text(strip=True))

# list comprehension을 써서 2차원 리스트로 만들기
result = [lists_td[i * 4:(i + 1) * 4] for i in range((len(lists_td) + 4 - 1) // 4 )]

# 리스트 정렬하기(3번째에 있는 숫자 오름차순으로)
result = sorted(result, key=lambda code: code[3])

# print(result)
# for idx_i, val_i in enumerate(result):
#   for idx_j, val_j in enumerate(val_i):
#     print(val_j)
# print(result)

# 2차원 리스트를 딕셔너리로 변환하기
dict_result = {}
dict_result = dict(zip(range(len(result)), result))
# print(dict_result.get(5)[2], dict_result.get(5)[3])


# exception
# print("That wasn't a number")
# print("Choose a number from the list.")

def select_country(dict_result) :
  print("Hello! Please choose select a country by number:")
  for code, cur in enumerate(dict_result):
    print("#",dict_result.get(code)[3], dict_result.get(code)[0])

def choose_country(dict_result) :
  select_country(dict_result)
  print('==========SELECT=========')
  choice = input("Choose a number from the list.\n#: ")
  try :
    for value_list in dict_result.values() :
      if choice in value_list :
        print("You chose ", end='')
        i = 0
        while i < len(value_list):
          x = value_list[i]
          if x == choice :
            print(value_list[1])
            print("The curreny code is " + value_list[2])
            break
          i += 1
  except : 
    print("That wasn't a number") 
  print('==========FINISH=========')

choose_country(dict_result)
