import random
key = '18sdqPnoqMEjN5FERbhv5tqJ%2BJzN7VX%2FMWseSnqgnxjcMc6rqTp%2FJZnI%2ByGiQo5ep9WI6%2F9oVMoqrMhvlHyCdA%3D%3D'

import requests
from bs4 import BeautifulSoup

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6'.format(key)
response = requests.get(url).text
data = BeautifulSoup(response, 'xml')
item = data('item')[5]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

print('{} 기준 {}의 미세먼지 농도는 {} 입니다.'.format(time, station, dust))

# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.

if dust > 150:
    print("매우 나쁨")
elif dust > 80 and dust <=150:
    print("나쁨")
elif dust >30 and dust <= 80:
    print("보통")
else:
    print("좋음")