import requests
f = open("request.txt", 'w')
f << requests.get('https://www.naver.com').text


f.close
