import requests
from bs4 import BeautifulSoup
# html 파일을 텍스트로 가져오기
market = requests.get('https://www.naver.com').text
# 텍스트로 가져온 html파일을 파이썬이 이해하기 쉽게 바꿔주기
result = BeautifulSoup(market, 'html.parser')
# copy selector
# 부모 자식의 관계는 > 로 표시, class는 .으로 표시
names = result.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li >a> .ah_k')
# 값만 표시
for i in range(0, len(names)):
    print(names[i].text)