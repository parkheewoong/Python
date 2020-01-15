import requests
from bs4 import BeautifulSoup
# html 파일을 텍스트로 가져오기
market = requests.get('https://finance.naver.com/marketindex/').text
# 텍스트로 가져온 html파일을 파이썬이 이해하기 쉽게 바꿔주기
result = BeautifulSoup(market, 'html.parser')
# copy selector
val = result.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
# 값만 표시
print(val.text)
