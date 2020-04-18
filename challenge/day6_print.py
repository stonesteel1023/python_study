import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency


print(format_currency(5000, "KRW", locale="ko_KR"))