import requests

def print_welcome():
    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLs you want to check.")

def write_url():
  print_welcome()
  print('==============START=============')
  url_list = []
  urls = input()
  urls = urls.split(',')
  for url in urls :
    url = url.strip()
    if 'http://' not in url :
      url = f'http://{url}'
      url_list.append(url)
    else :
      url_list.append(url)
  return url_list

def down_it() :
  while True :
    for result_url in write_url() :
      try :
        r = requests.get(result_url)
        if r.status_code == 200 :
          print (f'{result_url} is up')
      except :
        if '.com' not in result_url :
          result_url = result_url[7:]
          print(f'{result_url} is not a valid URL')
        else :
          print (f'{result_url} is down')
    reply = input('Do you want to start over? y/n\n=> ')
    if reply == "y" :
      continue
    elif reply == "n" :
      print('===============END===============')
      break
    else :
      print("not a vaild answer")
      reply = input('Do you want to start over? y/n\n=> ')
      if reply == "y" :
        continue
      elif reply == "n" :
        print('===============END==============')
        break

down_it()